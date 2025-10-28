"""
VA Visualizer Component
------------------------
实时显示 Valence/Arousal 值和可视化图表
"""

import sys
from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui


class VACanvas(QtWidgets.QWidget):
    """
    VA 可视化画布
    显示：
    1. 当前 V/A 数值
    2. 实时曲线图
    3. 2D 散点图
    """
    
    def __init__(self, parent=None, max_history=100):
        super().__init__(parent)
        # 确保有足够的空间显示所有内容
        self.setMinimumWidth(400)
        self.setMinimumHeight(700)
        
        self.max_history = max_history
        self.v_history = []  # 历史值列表
        self.a_history = []
        self.quadrants = []  # 历史象限
        
        self.v_label = QtWidgets.QLabel("Valence: 0.000")
        self.a_label = QtWidgets.QLabel("Arousal: 0.000")
        self.q_label = QtWidgets.QLabel("Quadrant: --")
        
        # 设置字体
        font = QtGui.QFont("Courier", 10)
        font.setBold(True)
        self.v_label.setFont(font)
        self.a_label.setFont(font)
        self.q_label.setFont(font)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(8)
        
        # 数值显示
        values_layout = QtWidgets.QVBoxLayout()
        values_layout.setSpacing(4)
        values_layout.addWidget(self.v_label)
        values_layout.addWidget(self.a_label)
        values_layout.addWidget(self.q_label)
        layout.addLayout(values_layout)
        
        # 添加分隔线
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(line)
        
        # 标签
        label = QtWidgets.QLabel("Real-time V/A Chart")
        label.setStyleSheet("font-weight: bold; color: #666;")
        layout.addWidget(label)
        
        self.setStyleSheet("""
            VACanvas {
                background: #1a1a1a;
            }
            QLabel {
                color: white;
                background: rgba(0,0,0,0.3);
                padding: 4px 8px;
                border-radius: 4px;
            }
        """)
    
    def update_va(self, v: float, a: float, quad: str):
        """更新 V/A 值"""
        # 更新历史
        self.v_history.append(v)
        self.a_history.append(a)
        self.quadrants.append(quad)
        
        # 限制历史长度
        if len(self.v_history) > self.max_history:
            self.v_history.pop(0)
            self.a_history.pop(0)
            self.quadrants.pop(0)
        
        # 更新标签
        color_v = "#4CAF50" if v > 0 else "#F44336"
        color_a = "#FF9800" if a > 0 else "#2196F3"
        
        self.v_label.setText(f'Valence: {v:+.3f}')
        self.v_label.setStyleSheet(f"color: {color_v}; background: rgba(0,0,0,0.3); padding: 4px 8px; border-radius: 4px;")
        
        self.a_label.setText(f'Arousal: {a:+.3f}')
        self.a_label.setStyleSheet(f"color: {color_a}; background: rgba(0,0,0,0.3); padding: 4px 8px; border-radius: 4px;")
        
        self.q_label.setText(f'Quadrant: {quad}')
        
        # 触发重绘
        self.update()
    
    def paintEvent(self, event):
        """绘制可视化图形"""
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        # 获取绘制区域
        rect = self.rect()
        
        # 计算可用空间（减去标签的高度）
        label_height = 90  # 标签区域高度
        padding = 10
        chart_area = QtCore.QRect(
            rect.left() + padding,
            rect.top() + label_height,
            rect.width() - 2 * padding,
            rect.height() - label_height - padding
        )
        
        # 如果图表区域太小或没有数据，不绘制
        if not self.v_history or chart_area.width() < 50 or chart_area.height() < 50:
            return
        
        # 绘制背景
        painter.fillRect(chart_area, QtGui.QColor(20, 20, 20))
        
        # 绘制网格
        painter.setPen(QtGui.QPen(QtGui.QColor(60, 60, 60), 1))
        mid_x = chart_area.center().x()
        mid_y = chart_area.center().y()
        painter.drawLine(chart_area.left(), mid_y, chart_area.right(), mid_y)
        painter.drawLine(mid_x, chart_area.top(), mid_x, chart_area.bottom())
        
        # 绘制坐标轴标签（移除冗余，仅保留象限标签）
        # 不绘制额外的 A+/A-/V+/V- 标签，避免冗余
        
        # 绘制最近的散点（显示 V/A 平面位置）
        if len(self.v_history) > 0:
            v_curr = self.v_history[-1]
            a_curr = self.a_history[-1]
            
            # 映射到屏幕坐标
            x = mid_x + v_curr * (chart_area.width() / 2 - 10)
            y = mid_y - a_curr * (chart_area.height() / 2 - 10)
            
            # 绘制象限背景色（简化版，使用浅色背景）
            for q_idx, (qx, qy, qw, qh) in enumerate([
                (chart_area.right() - 35, chart_area.top() + 5, 30, 25),   # Q1
                (chart_area.left() + 5, chart_area.top() + 5, 30, 25),     # Q2
                (chart_area.left() + 5, chart_area.bottom() - 30, 30, 25),  # Q3
                (chart_area.right() - 35, chart_area.bottom() - 30, 30, 25) # Q4
            ]):
                colors = [(76, 175, 80, 60), (244, 67, 54, 60), 
                         (156, 39, 176, 60), (33, 150, 243, 60)]
                r, g, b, a = colors[q_idx]
                q_rect = QtCore.QRect(qx, qy, qw, qh)
                painter.fillRect(q_rect, QtGui.QColor(r, g, b, a))
                painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255), 2))
                painter.setFont(QtGui.QFont("Arial", 9, QtGui.QFont.Bold))
                painter.drawText(q_rect, QtCore.Qt.AlignCenter, f"Q{q_idx+1}")
            
            # 绘制当前点（大圆圈）- 确保在有效范围内
            if chart_area.contains(QtCore.QPoint(int(x), int(y))):
                painter.setPen(QtGui.QPen(QtGui.QColor(255, 193, 7), 3))
                painter.setBrush(QtGui.QColor(255, 193, 7, 180))
                painter.drawEllipse(QtCore.QPointF(x, y), 8, 8)
            
            # 绘制历史轨迹（小点）
            if len(self.v_history) > 1:
                painter.setPen(QtCore.Qt.NoPen)
                
                # 只绘制最后20个点
                start = max(0, len(self.v_history) - 20)
                num_points = min(20, len(self.v_history) - start)
                
                for i in range(start, len(self.v_history)):
                    v_h = self.v_history[i]
                    a_h = self.a_history[i]
                    x_h = mid_x + v_h * (chart_area.width() / 2 - 10)
                    y_h = mid_y - a_h * (chart_area.height() / 2 - 10)
                    
                    # 确保在有效范围内
                    if chart_area.contains(QtCore.QPoint(int(x_h), int(y_h))):
                        # 越老的点越透明
                        alpha = int(60 * (i - start) / max(num_points, 1))
                        painter.setBrush(QtGui.QColor(255, 255, 255, max(10, alpha)))
                        painter.drawEllipse(QtCore.QPointF(x_h, y_h), 4, 4)


class VAGraphWidget(QtWidgets.QWidget):
    """带滚动条的历史曲线图"""
    
    def __init__(self, parent=None, max_history=100):
        super().__init__(parent)
        self.setMinimumHeight(150)
        
        self.max_history = max_history
        self.v_history = []
        self.a_history = []
        
    def update_data(self, v: float, a: float):
        """更新数据"""
        self.v_history.append(v)
        self.a_history.append(a)
        
        if len(self.v_history) > self.max_history:
            self.v_history.pop(0)
            self.a_history.pop(0)
        
        self.update()
    
    def paintEvent(self, event):
        """绘制曲线图"""
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        rect = self.rect()
        
        # 背景
        painter.fillRect(rect, QtGui.QColor(30, 30, 30))
        
        if len(self.v_history) < 2:
            return
        
        # 绘制网格
        painter.setPen(QtGui.QPen(QtGui.QColor(60, 60, 60), 1))
        mid_y = rect.height() // 2
        painter.drawLine(0, mid_y, rect.width(), mid_y)
        
        # 绘制 V 曲线（绿色）
        painter.setPen(QtGui.QPen(QtGui.QColor(76, 175, 80), 2))
        path_v = QtGui.QPainterPath()
        for i, v in enumerate(self.v_history):
            x = i * rect.width() / max(len(self.v_history) - 1, 1)
            y = mid_y - v * (rect.height() // 2 - 10)
            if i == 0:
                path_v.moveTo(x, y)
            else:
                path_v.lineTo(x, y)
        painter.drawPath(path_v)
        
        # 绘制 A 曲线（橙色）
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 152, 0), 2))
        path_a = QtGui.QPainterPath()
        for i, a in enumerate(self.a_history):
            x = i * rect.width() / max(len(self.v_history) - 1, 1)
            y = mid_y - a * (rect.height() // 2 - 10)
            if i == 0:
                path_a.moveTo(x, y)
            else:
                path_a.lineTo(x, y)
        painter.drawPath(path_a)
        
        # 绘制零线
        painter.setPen(QtGui.QPen(QtGui.QColor(100, 100, 100), 1))
        painter.drawLine(0, mid_y, rect.width(), mid_y)
        
        # 标签
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255)))
        painter.setFont(QtGui.QFont("Arial", 9))
        painter.drawText(10, 20, "V/A 变化曲线 (绿=V, 橙=A)")
        painter.drawText(10, rect.height() - 10, "-1.0")
        painter.drawText(10, 10, "+1.0")


if __name__ == "__main__":
    # 测试可视化组件
    app = QtWidgets.QApplication(sys.argv)
    
    widget = VACanvas()
    widget.show()
    
    import random
    import time
    
    def update_test():
        v = random.uniform(-1, 1)
        a = random.uniform(-1, 1)
        q = f"Q{random.randint(1, 4)}"
        widget.update_va(v, a, q)
    
    timer = QtCore.QTimer()
    timer.timeout.connect(update_test)
    timer.start(100)
    
    sys.exit(app.exec())

