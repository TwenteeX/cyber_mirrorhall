"""
Camera-Based HSEmotion Recognition Engine
------------------------------------------
Real-time emotion recognition using camera + HSEmotion library.
Outputs (valence, arousal) at ~10Hz with EMA smoothing.

Usage:
    from engine_hsemotion import HSECameraEngine
    engine = HSECameraEngine(cam_index=0, infer_hz=10)
    engine.sig_va.connect(your_handler)
    engine.start()
"""

import sys
import cv2
import numpy as np
from typing import Optional

from PySide6 import QtCore

try:
    from hsemotion.facial_emotions import HSEmotionRecognizer
    from facenet_pytorch import MTCNN
    _HS_AVAILABLE = True
except ImportError:
    _HS_AVAILABLE = False
    print("Warning: HSEmotion or facenet-pytorch not installed.")
    print("Install with: pip install hsemotion facenet-pytorch")

from emotion_va import probs_to_valence_arousal


class HSECameraEngine(QtCore.QObject):
    """
    Real-time emotion recognition engine using camera + HSEmotion.
    
    Captures frames from camera, runs HSEmotion inference, maps to V/A space,
    and applies EMA smoothing to reduce jitter.
    """
    
    sig_va = QtCore.Signal(float, float)  # Emits (valence, arousal)
    
    def __init__(self, 
                 cam_index: int = 0,
                 infer_hz: int = 10,
                 resize_width: int = 640,
                 ema_alpha: float = 0.15,
                 model_name: str = 'enet_b0_8_best_afew',
                 device: str = 'cpu',
                 parent: Optional[QtCore.QObject] = None):
        """
        Args:
            cam_index: Camera device index (0 for default)
            infer_hz: Inference frequency in Hz (frames per second)
            resize_width: Resize frame width for faster processing
            ema_alpha: EMA smoothing factor (0-1), lower = more smoothing
            model_name: HSEmotion model name
            device: 'cpu' or 'gpu'
            parent: Parent QObject
        """
        super().__init__(parent)
        
        if not _HS_AVAILABLE:
            raise ImportError("HSEmotion library not available. Install with: pip install hsemotion facenet-pytorch")
        
        self.cam_index = cam_index
        self.infer_hz = infer_hz
        self.resize_width = resize_width
        self.ema_alpha = ema_alpha
        
        # Camera and models
        self.cap: Optional[cv2.VideoCapture] = None
        self.fer = HSEmotionRecognizer(model_name=model_name, device=device)
        self.mtcnn = MTCNN(keep_all=True, device=device)
        
        # EMA state
        self.v_ema = 0.0  # valence exponential moving average
        self.a_ema = 0.0  # arousal exponential moving average
        
        # Baseline calibration
        self.baseline_v = 0.0  # neutral baseline for valence
        self.baseline_a = 0.0  # neutral baseline for arousal
        self.baseline_samples = []  # Collect samples for baseline
        self.baseline_collecting = False  # Flag for baseline collection mode
        
        # Confidence threshold
        self.confidence_threshold = 0.35  # Minimum max probability to accept
        
        # Gain factors for baseline correction
        self.gain_v = 1.5  # Valence gain
        self.gain_a = 1.5  # Arousal gain
        
        # Timer for periodic inference
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(int(1000 / infer_hz))  # Convert Hz to ms
        self.timer.timeout.connect(self._step)
        
        # Frame counter for optional status updates
        self.frame_count = 0
        
    def start(self, collect_baseline: bool = True, baseline_duration: float = 3.0):
        """
        Start camera capture and begin inference loop
        
        Args:
            collect_baseline: If True, collect neutral baseline for 3-5 seconds
            baseline_duration: Duration in seconds to collect baseline
        """
        self.cap = cv2.VideoCapture(self.cam_index)
        
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open camera {self.cam_index}")
        
        print(f"Camera opened: index={self.cam_index}, inference={self.infer_hz}Hz")
        
        # Start baseline collection if requested
        if collect_baseline:
            self.baseline_collecting = True
            self.baseline_samples = []
            baseline_frames = int(baseline_duration * self.infer_hz)
            print(f"Collecting baseline for {baseline_duration}s ({baseline_frames} frames)...")
            print("Please maintain a neutral expression.")
        
        self.timer.start()
    
    def stop(self):
        """Stop camera and timer"""
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None
    
    def _step(self):
        """Process one frame: capture, infer, smooth, emit"""
        if not self.cap or not self.cap.isOpened():
            return
        
        # Capture frame
        ret, frame = self.cap.read()
        if not ret:
            # Camera failure - slowly decay to neutral
            self.v_ema *= 0.98
            self.a_ema *= 0.98
            self.sig_va.emit(float(self.v_ema), float(self.a_ema))
            return
        
        self.frame_count += 1
        
        # Resize for faster inference
        height, width = frame.shape[:2]
        if width > self.resize_width:
            scale = self.resize_width / width
            new_height = int(height * scale)
            frame = cv2.resize(frame, (self.resize_width, new_height))
        
        # Run face detection and emotion recognition
        try:
            # Convert BGR to RGB for facenet
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Detect faces
            boxes, probs = self.mtcnn.detect(rgb_frame)
            
            if boxes is None or len(boxes) == 0:
                # No face detected - slowly decay to neutral
                self.v_ema *= 0.98
                self.a_ema *= 0.98
                self.sig_va.emit(float(self.v_ema), float(self.a_ema))
                return
            
            # Get the most confident face
            best_idx = np.argmax(probs) if len(probs) > 0 else 0
            box = boxes[best_idx]
            confidence = probs[best_idx]
            
            # Check confidence threshold
            if confidence < self.confidence_threshold:
                # Low confidence - slowly decay
                self.v_ema *= 0.98
                self.a_ema *= 0.98
                self.sig_va.emit(float(self.v_ema), float(self.a_ema))
                return
            
            # Extract face region
            x1, y1, x2, y2 = [int(b) for b in box]
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(rgb_frame.shape[1], x2)
            y2 = min(rgb_frame.shape[0], y2)
            
            face_img = rgb_frame[y1:y2, x1:x2]
            
            # Run HSEmotion recognition
            emotion, scores = self.fer.predict_emotions(face_img, logits=False)
            
            # Convert HSEmotion output to FER format for consistency
            emotion_probs = self._convert_hs_to_fer_format(emotion, scores)
            
            # Map to V/A space
            v, a = probs_to_valence_arousal(emotion_probs)
            
            # Baseline collection mode
            if self.baseline_collecting:
                self.baseline_samples.append((v, a))
                baseline_frames_needed = int(3.0 * self.infer_hz)  # 3 seconds
                
                if len(self.baseline_samples) >= baseline_frames_needed:
                    # Calculate baseline as median
                    baseline_samples_v = [s[0] for s in self.baseline_samples]
                    baseline_samples_a = [s[1] for s in self.baseline_samples]
                    baseline_samples_v.sort()
                    baseline_samples_a.sort()
                    
                    self.baseline_v = baseline_samples_v[len(baseline_samples_v) // 2]
                    self.baseline_a = baseline_samples_a[len(baseline_samples_a) // 2]
                    
                    self.baseline_collecting = False
                    print(f"Baseline established: V={self.baseline_v:.3f}, A={self.baseline_a:.3f}")
                    self.baseline_samples = []
            
            # Apply baseline correction: v_corr = gain * (v - v0)
            v_corrected = self.gain_v * (v - self.baseline_v)
            a_corrected = self.gain_a * (a - self.baseline_a)
            
            # Clamp to [-1, 1]
            v_corrected = np.clip(v_corrected, -1.0, 1.0)
            a_corrected = np.clip(a_corrected, -1.0, 1.0)
            
            # Apply EMA smoothing
            self.v_ema = self.ema_alpha * v_corrected + (1 - self.ema_alpha) * self.v_ema
            self.a_ema = self.ema_alpha * a_corrected + (1 - self.ema_alpha) * self.a_ema
            
        except Exception as e:
            print(f"HSEmotion inference error: {e}")
            self.v_ema *= 0.98
            self.a_ema *= 0.98
        
        # Emit smoothed V/A values
        self.sig_va.emit(float(self.v_ema), float(self.a_ema))
    
    def _convert_hs_to_fer_format(self, emotion: str, scores: dict) -> dict:
        """
        Convert HSEmotion output to FER format.
        
        HSEmotion emotions: angry, contempt, disgust, fear, happy, neutral, sad, surprise
        FER format expects: angry, disgust, fear, happy, sad, surprise, neutral
        """
        # Initialize with zeros
        fer_probs = {
            'angry': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'happy': 0.0,
            'sad': 0.0,
            'surprise': 0.0,
            'neutral': 0.0
        }
        
        # Map HSEmotion emotions to FER format
        emotion_map = {
            'angry': 'angry',
            'contempt': 'angry',  # contempt maps to angry
            'disgust': 'disgust',
            'fear': 'fear',
            'happy': 'happy',
            'neutral': 'neutral',
            'sad': 'sad',
            'surprise': 'surprise'
        }
        
        # Convert scores dictionary to our format
        if isinstance(scores, dict):
            for hs_emotion, prob in scores.items():
                fer_key = emotion_map.get(hs_emotion)
                if fer_key and fer_key in fer_probs:
                    if fer_key == 'angry':
                        fer_probs['angry'] += prob  # Add contempt to angry
                    else:
                        fer_probs[fer_key] = prob
        
        return fer_probs
    
    def __del__(self):
        """Clean up resources"""
        self.stop()


if __name__ == "__main__":
    # Simple test if run directly
    print("Starting HSEmotion engine test...")
    print("Press Ctrl+C to stop")
    
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    try:
        engine = HSECameraEngine(cam_index=0, infer_hz=5)
        
        def on_va(v, a):
            print(f"V={v:+.3f}, A={a:+.3f}")
        
        engine.sig_va.connect(on_va)
        engine.start()
        
        # Run for a few seconds
        QtCore.QTimer.singleShot(10000, app.quit)  # 10 seconds
        
        app.exec()
    except Exception as e:
        print(f"Error: {e}")

