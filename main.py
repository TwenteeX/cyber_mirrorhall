
# Nine-Grid AV Persona Skeleton (PySide6 + python-vlc)
# ----------------------------------------------------
# Installation:
#   1. Required: pip install -U PySide6 python-vlc
#   2. Install VLC desktop app so python-vlc can find libvlc (https://www.videolan.org/vlc/).
#      Windows: default install works. macOS: brew install --cask vlc. Linux: use package manager.
#
#   3. Optional (for camera emotion recognition):
#      pip install opencv-python fer
#
# Assets: put your 4 quadrant clips into assets/persona_00..08 as Q1.mp4 .. Q4.mp4
#
# Controls:
#   - This demo runs in "DEMO_MODE" (random V/A) by default; no camera needed.
#   - To use camera emotion recognition:
#     1. Install dependencies: pip install opencv-python fer
#     2. Set USE_CAMERA_EMOTION = True in this file
#     3. Run the program - it will use your camera for real-time emotion detection
#   - Press 1/2/3/4 to force all personas to a quadrant immediately.
#   - Press Space to toggle "switch at loop boundary" vs "immediate switch".
#
# Author: ChatGPT (GPT-5 Thinking)

import os
import sys
import random
import time
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from PySide6 import QtCore, QtWidgets, QtGui

import vlc  # python-vlc

# Import VA visualizer
try:
    from va_visualizer import VACanvas
    _VA_VIS_OK = True
except ImportError:
    _VA_VIS_OK = False
    print("Note: VA visualizer not available")

# ----------------- Config -----------------
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
GRID_ROWS = 3  # 改为竖向排列：9行1列
GRID_COLS = 3
PERSONA_TYPES = [
    "mirror", "oppose", "amplify",
    "performer", "cheer", "downer",
    "jitter", "smooth", "echo"
]
DEMO_MODE = True      # True: simulate valence/arousal; False: (optional) plug real emotion here
WAIT_FOR_BOUNDARY = True  # True: switch video only at loop edges; Space toggles during runtime

# Camera-based emotion recognition switch
USE_CAMERA_EMOTION = True  # Set to True to use camera + FER instead of demo mode

# Try to import camera engine, but don't fail if not available
# Try HSEmotion first, fallback to FER
try:
    from engine_hsemotion import HSECameraEngine
    _HS_CAM_OK = True
    _FER_CAM_OK = False
except ImportError:
    _HS_CAM_OK = False
    try:
        from engine_fer import CameraEmotionEngine
        _FER_CAM_OK = True
    except ImportError:
        _FER_CAM_OK = False
        print("Note: Camera emotion engine not available (missing dependencies)")
        print("For HSEmotion: pip install hsemotion facenet-pytorch")
        print("For FER fallback: pip install opencv-python fer")
_CAM_OK = _HS_CAM_OK or _FER_CAM_OK

VALENCE_TH = 0.20
AROUSAL_TH = 0.30
HYSTERESIS = 0.05

# -------- Persona transforms (control-ish spice) --------
def persona_transform(p_type: str, v: float, a: float, state: Dict) -> Tuple[float, float]:
    # state can store per-persona memory (for smooth/echo)
    if p_type == "mirror":
        return v, a
    elif p_type == "oppose":
        return -v, a
    elif p_type == "amplify":
        return clamp(1.5*v, -1, 1), clamp(1.2*a, -1, 1)
    elif p_type == "performer":
        # theatrical extremes
        vv = 1.0 if v > 0 else -1.0
        aa = 1.0 if abs(v) > 0.4 and a > 0.3 else a
        return vv, clamp(aa, -1, 1)
    elif p_type == "cheer":
        return clamp(0.6*v + 0.4, -1, 1), a
    elif p_type == "downer":
        return clamp(0.6*v - 0.4, -1, 1), a
    elif p_type == "jitter":
        return clamp(v + random.gauss(0, 0.15), -1, 1), clamp(a + random.gauss(0, 0.15), -1, 1)
    elif p_type == "smooth":
        pv, pa = state.get("va", (0.0, 0.0))
        nv = 0.85*pv + 0.15*v
        na = 0.85*pa + 0.15*a
        state["va"] = (nv, na)
        return nv, na
    elif p_type == "echo":
        # delayed response
        queue = state.setdefault("queue", [])
        queue.append((v, a))
        if len(queue) > 8:
            va = queue.pop(0)
        else:
            va = (0.0, 0.0)
        return va
    return v, a

def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x

def classify_quadrant(v: float, a: float, prev_q: Optional[str]) -> str:
    # with hysteresis/deadzone
    vth = VALENCE_TH
    ath = AROUSAL_TH
    if prev_q == "Q1":
        vth += HYSTERESIS; ath += HYSTERESIS
    elif prev_q == "Q2":
        vth += HYSTERESIS; ath += HYSTERESIS
    elif prev_q == "Q3":
        vth += HYSTERESIS; ath += HYSTERESIS
    elif prev_q == "Q4":
        vth += HYSTERESIS; ath += HYSTERESIS

    if v >=  vth and a >=  ath: return "Q1"
    if v <= -vth and a >=  ath: return "Q2"
    if v <= -vth and a <= -ath: return "Q3"
    if v >=  vth and a <= -ath: return "Q4"
    return prev_q or "Q4"

# ----------------- VLC Video Cell -----------------
class VideoCell(QtWidgets.QFrame):
    def __init__(self, parent=None, title="", background_image=None):
        super().__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setStyleSheet("background:#000;")
        
        # 创建垂直布局：标题栏 + 视频区域
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 顶部标题栏
        self.title_label = QtWidgets.QLabel(title)
        self.title_label.setStyleSheet("color:white; background:rgba(0,0,0,0.85); padding:4px 8px; font-weight:bold;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setMaximumHeight(35)
        layout.addWidget(self.title_label)
        
        # 视频容器（用于 VLC 渲染）
        self.video_container = QtWidgets.QFrame()
        self.video_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_container.setStyleSheet("background:#000;")
        layout.addWidget(self.video_container, stretch=1)
        
        # 在视频容器中加载背景图片
        self.image_label = QtWidgets.QLabel(self.video_container)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # 加载背景图片
        if background_image and os.path.exists(background_image):
            self._load_background_image(background_image)

    def _load_background_image(self, image_path):
        """加载并显示背景图片，适应竖版图片"""
        pixmap = QtGui.QPixmap(image_path)
        if not pixmap.isNull():
            self.background_pixmap = pixmap
            self._update_background_image()
    
    def _update_background_image(self):
        """更新背景图片大小"""
        if not hasattr(self, 'background_pixmap'):
            return
        
        size = self.video_container.size()
        if size.width() < 10 or size.height() < 10:
            return
        
        # 竖版图片需要适配横版格子
        # 保持竖版图片的纵横比，填充到横版格子
        target_width = size.width()
        target_height = size.height()
        
        # 计算缩放比例，使图片完全填充格子（可能裁剪）
        pixmap_width = self.background_pixmap.width()
        pixmap_height = self.background_pixmap.height()
        
        # 计算缩放比例，确保填满整个格子
        scale_w = target_width / pixmap_width
        scale_h = target_height / pixmap_height
        
        # 使用较大的比例，确保填满
        scale = max(scale_w, scale_h)
        
        scaled_pixmap = self.background_pixmap.scaled(
            target_width,
            target_height,
            QtCore.Qt.KeepAspectRatioByExpanding,  # 扩展填充
            QtCore.Qt.SmoothTransformation
        )
        
        self.image_label.setPixmap(scaled_pixmap)
        # 居中显示
        self.image_label.resize(size)
        self.image_label.move(0, 0)

    def resizeEvent(self, e):
        # 更新背景图片
        if hasattr(self, 'background_pixmap'):
            QtCore.QTimer.singleShot(10, self._update_background_image)
        super().resizeEvent(e)

# ----------------- Persona Player -----------------
class PersonaPlayer(QtCore.QObject):
    sig_update_label = QtCore.Signal(str)
    sig_ended = QtCore.Signal(int)  # emits player index when media ends

    def __init__(self, idx: int, persona_type: str, video_widget: VideoCell, vlc_instance: vlc.Instance, media_map: Dict[str, str]):
        super().__init__()
        self.idx = idx
        self.p_type = persona_type
        self.widget = video_widget
        self.instance = vlc_instance
        self.media_map = media_map

        self.player = self.instance.media_player_new()

        # Window handle for VLC rendering - use video_container instead of widget
        if sys.platform.startswith("linux"):   # X11
            self.player.set_xwindow(int(self.widget.video_container.winId()))
        elif sys.platform == "win32":
            self.player.set_hwnd(int(self.widget.video_container.winId()))
        elif sys.platform == "darwin":
            self.player.set_nsobject(int(self.widget.video_container.winId()))
        else:
            print("Unsupported platform for VLC video output")

        self.curr_quad: Optional[str] = None
        self.next_quad: Optional[str] = None
        self.state: Dict = {}   # persona transform memory
        self.external_end_control: bool = False  # when True, MainWindow decides next clip on end

        # VLC end event -> handle loop/switch
        self.em = self.player.event_manager()
        self.em.event_attach(vlc.EventType.MediaPlayerEndReached, self._on_end)

        self.sig_update_label.connect(self._set_label_text)

        self._update_label()

    def _set_label_text(self, txt: str):
        self.widget.title_label.setText(txt)

    def _update_label(self):
        text = f"#{self.idx:02d}  {self.p_type}\n{self.curr_quad or '--'}"
        self.sig_update_label.emit(text)

    def start(self, initial_quad="Q4"):
        self.curr_quad = initial_quad
        self._play_quad(self.curr_quad)

    def _play_quad(self, quad: str):
        path = self.media_map.get(quad)
        if not path or not os.path.exists(path):
            # Graceful fallback: black
            self.player.stop()
            self._update_label()
            return
        media = self.instance.media_new(path)
        self.player.set_media(media)
        self.player.play()
        self._update_label()

    def request_quad(self, quad: str, immediate: bool):
        if immediate:
            # switch right now
            self.curr_quad = quad
            self.next_quad = None
            self._play_quad(self.curr_quad)
        else:
            # mark and switch at boundary
            self.next_quad = quad

    def _on_end(self, event):
        # Called in VLC thread; use Qt to schedule safely
        QtCore.QMetaObject.invokeMethod(self, "_handle_end", QtCore.Qt.QueuedConnection)

    @QtCore.Slot()
    def _handle_end(self):
        if self.external_end_control:
            # Let MainWindow decide what to play next
            self.sig_ended.emit(self.idx)
            return
        target = self.next_quad or self.curr_quad or "Q4"
        self.curr_quad = target
        self.next_quad = None
        self._play_quad(self.curr_quad)

# ----------------- Emotion Engine (Demo) -----------------
class EmotionEngine(QtCore.QObject):
    """Produces a global valence/arousal (v,a) in [-1,1] with a smooth random walk.
       Replace with FER/DeepFace integration if needed.
    """
    sig_va = QtCore.Signal(float, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.v = 0.0
        self.a = 0.0
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)  # 10 Hz
        self.timer.timeout.connect(self._step)

    def start(self):
        self.timer.start()

    def _step(self):
        # smooth random walk
        self.v = clamp(self.v + random.gauss(0, 0.05), -1, 1)
        self.a = clamp(self.a + random.gauss(0, 0.05), -1, 1)
        self.sig_va.emit(self.v, self.a)

# ----------------- Main Window -----------------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nine-Grid Personas (PySide6 + python-vlc)")
        self.resize(1600, 1000)  # 调整窗口尺寸以适应竖向布局

        central = QtWidgets.QWidget(self)
        self.setCentralWidget(central)

        # 主布局：水平布局（左侧视频网格，右侧可视化）
        main_layout = QtWidgets.QHBoxLayout(central)
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(6,6,6,6)
        
        # 左侧：视频网格
        grid_widget = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(grid_widget)
        grid.setSpacing(4)
        grid.setContentsMargins(0,0,0,0)
        
        # 设置每个格子的固定尺寸（横版比例 4:3）
        self.cell_aspect_ratio = (640, 480)  # 宽:高

        self.vlc_instance = vlc.Instance()

        self.cells = []
        self.players: list[PersonaPlayer] = []
        
        # Dominant quadrant decision window (rolling buffer)
        self.history_window_secs = 3.0
        self.history_maxlen = int(self.history_window_secs * 10)  # engine ~10Hz
        self.quad_history: list[str] = []
        self.use_dominant_logic = True

        # Build grid
        idx = 0
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                title = f"#{idx:02d}"
                
                # 加载 neutral.png 作为背景
                neutral_path = os.path.join(ASSETS_DIR, f"persona_{idx:02d}", "neutral.png")
                cell = VideoCell(self, title=title, background_image=neutral_path)
                
                # 设置固定尺寸为横版比例（4:3）
                cell.setMinimumSize(320, 240)  # 最小尺寸
                cell.setMaximumSize(640, 480)  # 最大尺寸
                cell.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                
                self.cells.append(cell)
                grid.addWidget(cell, r, c)

                ptype = PERSONA_TYPES[idx % len(PERSONA_TYPES)]
                media_map = self._load_media_map(idx)
                player = PersonaPlayer(idx, ptype, cell, self.vlc_instance, media_map)
                self.players.append(player)
                idx += 1

        # Start all
        for p in self.players:
            p.start(initial_quad="Q4")
            # enable external end control so we decide clip after each end
            p.external_end_control = True
            p.sig_ended.connect(self._on_player_end)

        # 添加视频网格到主布局（左侧，竖向排列）
        main_layout.addWidget(grid_widget, stretch=2)
        
        # 右侧：VA 可视化面板
        if _VA_VIS_OK:
            self.va_visualizer = VACanvas(parent=self)
            self.va_visualizer.setMinimumWidth(400)
            self.va_visualizer.setFixedWidth(400)  # 固定宽度
            main_layout.addWidget(self.va_visualizer, stretch=1)
            
            # 初始化显示
            self.va_visualizer.update_va(0.0, 0.0, "Q4")
        else:
            self.va_visualizer = None

        self.status = self.statusBar()
        self.current_quadrant = "Q4"  # 当前象限

        # Emotion engine - choose between camera+HSEmotion, camera+FER or demo mode
        if USE_CAMERA_EMOTION and _CAM_OK:
            try:
                if _HS_CAM_OK:
                    self.engine = HSECameraEngine(cam_index=0, infer_hz=10, parent=self)
                    self.status.showMessage("Mode: CAMERA+HSEmotion | Space: toggle boundary-switch | 1-4: force quadrant")
                elif _FER_CAM_OK:
                    self.engine = CameraEmotionEngine(cam_index=0, infer_hz=10, parent=self)
                    self.status.showMessage("Mode: CAMERA+FER | Space: toggle boundary-switch | 1-4: force quadrant")
            except Exception as e:
                print(f"Failed to start camera engine: {e}")
                print("Falling back to demo mode...")
                self.engine = EmotionEngine(self)
                self.status.showMessage("Mode: DEMO (fallback) | Space: toggle boundary-switch | 1-4: force quadrant")
        else:
            self.engine = EmotionEngine(self)
            self.status.showMessage("Mode: DEMO | Space: toggle boundary-switch | 1-4: force quadrant")
        
        self.engine.sig_va.connect(self.on_va)
        self.engine.start()

        self.wait_for_boundary = WAIT_FOR_BOUNDARY

    def _load_media_map(self, idx: int) -> Dict[str, str]:
        base = os.path.join(ASSETS_DIR, f"persona_{idx:02d}")
        # Prefer persona-indexed files P{idx}_Q*.mp4 if present (all personas support this now)
        persona_tag = f"P{idx}_"
        candidates = {
            "Q1": os.path.join(base, f"{persona_tag}Q1.mp4"),
            "Q2": os.path.join(base, f"{persona_tag}Q2.mp4"),
            "Q3": os.path.join(base, f"{persona_tag}Q3.mp4"),
            "Q4": os.path.join(base, f"{persona_tag}Q4.mp4"),
        }
        # Fallback to Q*.mp4
        fallback = {
            "Q1": os.path.join(base, "Q1.mp4"),
            "Q2": os.path.join(base, "Q2.mp4"),
            "Q3": os.path.join(base, "Q3.mp4"),
            "Q4": os.path.join(base, "Q4.mp4"),
        }
        media_map: Dict[str, str] = {}
        for q, path in candidates.items():
            media_map[q] = path if os.path.exists(path) else fallback[q]
        return media_map

    @QtCore.Slot(float, float)
    def on_va(self, v: float, a: float):
        # 更新可视化面板
        if self.va_visualizer:
            self.va_visualizer.update_va(v, a, self.current_quadrant)
        
        # 记录历史象限（按第一个 persona 的分类，以保持一致性）
        vv0, aa0 = persona_transform(self.players[0].p_type, v, a, self.players[0].state)
        q0 = classify_quadrant(vv0, aa0, self.players[0].curr_quad)
        self.quad_history.append(q0)
        if len(self.quad_history) > self.history_maxlen:
            self.quad_history.pop(0)
        self.current_quadrant = q0
        
        # 即时切换禁用：由结束回调决定（external_end_control=True）
        if not self.use_dominant_logic:
            for p in self.players:
                vv, aa = persona_transform(p.p_type, v, a, p.state)
                next_q = classify_quadrant(vv, aa, p.curr_quad)
                if next_q and next_q != p.curr_quad:
                    p.request_quad(next_q, immediate=not self.wait_for_boundary)

    # -------------- Key controls --------------
    def keyPressEvent(self, e: QtGui.QKeyEvent):
        if e.key() == QtCore.Qt.Key_Space:
            self.wait_for_boundary = not self.wait_for_boundary
            self.status.showMessage(f"Boundary switch: {self.wait_for_boundary}")
        elif e.key() in (QtCore.Qt.Key_1, QtCore.Qt.Key_2, QtCore.Qt.Key_3, QtCore.Qt.Key_4):
            q = {QtCore.Qt.Key_1:"Q1", QtCore.Qt.Key_2:"Q2",
                 QtCore.Qt.Key_3:"Q3", QtCore.Qt.Key_4:"Q4"}[e.key()]
            for p in self.players:
                p.request_quad(q, immediate=True)
            self.current_quadrant = q  # 更新当前象限
            self.status.showMessage(f"Forced all to {q} (immediate)")
        else:
            super().keyPressEvent(e)

    def _dominant_quadrant(self) -> str:
        if not self.quad_history:
            return "Q4"
        counts: Dict[str, int] = {"Q1":0, "Q2":0, "Q3":0, "Q4":0}
        for q in self.quad_history:
            if q in counts:
                counts[q] += 1
        # tie-breaker preference: Q4 > Q1 > Q2 > Q3
        order = ["Q4","Q1","Q2","Q3"]
        return max(order, key=lambda q: counts[q])

    @QtCore.Slot(int)
    def _on_player_end(self, idx: int):
        # 每个播放器结束时，统一根据历史窗口的主导象限进行下一次播放
        dom_q = self._dominant_quadrant()
        for p in self.players:
            # Personas 0,1,3,4 有专用 P{idx}_Q*.mp4 文件已在 _load_media_map 处理中
            p.request_quad(dom_q, immediate=True)

# ----------------- Entrypoint -----------------
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
