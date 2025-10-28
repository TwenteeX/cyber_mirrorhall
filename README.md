
# Nine-Grid AV Persona Emotion-Driven Video System

## 0) What you get
- A runnable PySide6 window with a 3×3 grid, each cell displays persona-specific videos
- Real-time V/A visualization panel showing current valence/arousal values and 2D position
- **Three emotion recognition modes**:
  - **HSEmotion** (default): Advanced deep learning-based emotion recognition
  - **FER**: Traditional facial emotion recognition (fallback)
  - **DEMO**: Random emotion simulation (no camera needed)
- Each persona applies different emotion transforms (mirror/oppose/amplify/performer/cheer/downer/jitter/smooth/echo)
- **Dominant quadrant logic**: Videos switch based on your most frequent emotion quadrant (last 3 seconds)
- Each cell has a **title bar** showing persona info and current quadrant
- Video switching happens at loop boundaries to prevent tearing (Space toggles mode)

## 1) Install

### Required
```bash
pip install -U PySide6 python-vlc
```

Install VLC desktop player (libvlc provider):
- Windows: https://www.videolan.org/vlc/ (default install works)
- macOS: `brew install --cask vlc`
- Linux: use your package manager (e.g., `sudo apt install vlc`)

### Optional (for camera emotion recognition)
**Option A - HSEmotion (Recommended):**
```bash
pip install hsemotion facenet-pytorch
```

**Option B - FER (Alternative):**
```bash
pip install opencv-python fer
```

## 2) Folder layout
```
av-grid/
  main.py
  assets/
    persona_00/
      neutral.png        # Background image for each persona
      Q1.mp4  Q2.mp4     # Default videos
      Q3.mp4  Q4.mp4
      # Optional: persona-specific videos for P0, P1, P3, P4
      P0_Q1.mp4  P0_Q2.mp4  P0_Q3.mp4  P0_Q4.mp4
    persona_01/
      neutral.png
      Q1.mp4  Q2.mp4  Q3.mp4  Q4.mp4
      P1_Q1.mp4  P1_Q2.mp4  P1_Q3.mp4  P1_Q4.mp4  # Optional
    ...
    persona_08/
      neutral.png  # Recommended for all personas
      Q1.mp4  Q2.mp4  Q3.mp4  Q4.mp4
```

**Tips for clips:**
- 3–6 seconds, loopable if possible; H.264; same fps across all four per persona
- **Resolution**: Recommended 480p (640×480) or higher for 4:3 aspect ratio
- Q1: valence>0, arousal>0  (Happy+Excited) - 开心+激动
- Q2: valence<0, arousal>0  (Negative+Agitated) - 愤怒/惊恐
- Q3: valence<0, arousal<0  (Negative+Calm) - 沮丧/阴郁
- Q4: valence>0, arousal<0  (Positive+Relaxed) - 平静/满足

**Naming convention:**
- For personas 0, 1, 3, 4: Use `P{idx}_Q*.mp4` for unique videos per persona
- For others: Use standard `Q*.mp4`

## 3) Run
```bash
cd av-grid
python main.py
```

**Hotkeys:**
- `Space` – toggle switch-at-boundary (recommended) vs immediate switch
- `1/2/3/4` – force all cells to Q1/Q2/Q3/Q4 immediately (for testing)

**Interface:**
- **Top bar**: Each cell shows persona number, type, and current quadrant
- **Video area**: Main playback area below the title bar
- **Right panel**: Real-time V/A visualization with current values and 2D position

## 4) Emotion Recognition Modes

The system supports three modes with automatic fallback:

### Default Behavior
The program automatically detects and uses the best available engine:
```
HSEmotion → FER → DEMO
```

### Mode 1: HSEmotion (Recommended)
**What it does:** Advanced deep learning-based emotion recognition with 8 emotion categories

**Setup:**
```bash
pip install hsemotion facenet-pytorch
```

**Features:**
- Higher accuracy than FER
- 8 emotion types (angry, contempt, disgust, fear, happy, neutral, sad, surprise)
- Uses MTCNN for stable face detection
- Better handling of complex facial expressions

**Usage:**
- Set `USE_CAMERA_EMOTION = True` in `main.py`
- Run the program - it will detect and use HSEmotion automatically
- Status bar shows: "Mode: CAMERA+HSEmotion"

### Mode 2: FER (Fallback)
**What it does:** Traditional FER-based emotion recognition

**Setup:**
```bash
pip install opencv-python fer
```

**Features:**
- Fast and stable
- 7 emotion types
- Lower accuracy than HSEmotion but still effective

**Usage:**
- Automatically used if HSEmotion is not available
- Status bar shows: "Mode: CAMERA+FER"

### Mode 3: DEMO (Default)
**What it does:** Simulates random valence/arousal values at 10Hz

**Features:**
- No camera needed
- Useful for testing and development
- Smooth random walk in V/A space

**How it works:**
- Generates random V/A values using smooth random walk
- Values gradually change within [-1, 1] range
- Good for testing the 9 personas without camera

### How Emotion Recognition Works

1. **Capture**: Camera captures frames at 10Hz
2. **Detection**: Face is detected using MTCNN or built-in detector
3. **Recognition**: Emotions are classified using HSEmotion or FER
4. **Mapping**: Emotion probabilities mapped to Valence/Arousal using `emotion_va.py`
5. **Calibration**: 3-second baseline collection adjusts for individual differences
6. **Smoothing**: EMA smoothing reduces jitter (α=0.15)
7. **Visualization**: Right panel shows real-time V/A values and 2D position
8. **Personas**: Each persona applies its own emotion transform
9. **Quadrants**: Emotions map to 4 quadrants based on V/A thresholds
10. **Playback**: Videos switch based on dominant quadrant in last 3 seconds

### Troubleshooting

**Camera issues:**
- Ensure no other app is using the camera
- Check lighting - even, front-facing light works best
- Try different camera indices if you have multiple

**Performance:**
- Lower `infer_hz` from 10 to 5-8 Hz if CPU usage is too high
- Reduce `resize_width` from 640 to 320 for faster processing
- Use CPU mode if GPU is slow

**Recognition accuracy:**
- Maintain neutral expression for 3 seconds at startup (baseline collection)
- Face the camera directly
- Ensure good lighting without shadows

**Files:**
- `emotion_va.py`: Maps emotion probabilities to Valence/Arousal with probability sharpening
- `engine_hsemotion.py`: HSEmotion camera engine with baseline calibration
- `engine_fer.py`: FER camera engine (fallback)
- `va_visualizer.py`: Real-time V/A visualization panel
- `main.py`: Integrates all engines with automatic fallback

## 5) Advanced Features

### Dominant Quadrant Logic
- System tracks your emotional state over a 3-second window
- At video completion, plays the quadrant that appeared most frequently
- Prevents rapid switching and provides smoother experience

### Persona-Specific Videos
- For personas 0, 1, 3, 4: Place videos as `P{idx}_Q*.mp4` for unique content
- Example: `P0_Q1.mp4`, `P1_Q2.mp4`, etc.
- Other personas use standard `Q*.mp4` files

### Emotion Processing Improvements
- **Probability sharpening**: Emphasizes dominant emotions (sharp=1.8)
- **Baseline calibration**: 3-second neutral expression establishes your baseline
- **EMA smoothing**: Reduces jitter (α=0.15)
- **Confidence threshold**: Filters low-quality detections (threshold=0.35)
- **Weight balancing**: Adjusted weights prevent V/A values from clustering in negative range

### Configuration Options

**In `main.py`:**
```python
USE_CAMERA_EMOTION = True  # Enable camera mode
VALENCE_TH = 0.20          # Valence threshold
AROUSAL_TH = 0.30          # Arousal threshold
HYSTERESIS = 0.05          # Hysteresis for stability
```

**In emotion engines:**
```python
infer_hz = 10              # Recognition frequency
resize_width = 640        # Frame width
ema_alpha = 0.15          # Smoothing factor
confidence_threshold = 0.35  # Confidence threshold
gain_v = 1.5              # Valence gain
gain_a = 1.5              # Arousal gain
```

## 6) Notes
- **Black cells**: Check that Q*.mp4 or P*_Q*.mp4 files exist in persona folders
- **Performance**: Start with 480p; scale up after confirming performance
- **Camera not working**: Program falls back to DEMO mode automatically
- **Video switching**: Uses dominant quadrant logic at loop boundaries for smooth playback
- **Layout**: Each cell has a fixed title bar (35px) showing persona info, video plays below
