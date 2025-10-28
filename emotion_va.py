"""
FER Emotion Probabilities to Valence/Arousal Mapping
----------------------------------------------------
This module maps FER output probabilities to valence and arousal values
in the range [-1, 1].

Input: FER emotion probabilities dictionary
Output: (valence, arousal) tuple in [-1, 1]
"""

import numpy as np
from typing import Dict


def probs_to_valence_arousal(emotion_probs: Dict[str, float], sharp: float = 1.8) -> tuple[float, float]:
    """
    Map FER emotion probabilities to valence/arousal space with probability sharpening.
    
    Args:
        emotion_probs: Dict with keys like 'angry', 'disgust', 'fear', 
                      'happy', 'sad', 'surprise', 'neutral'
        sharp: Probability sharpening factor (1.6-2.0 recommended)
    
    Returns:
        (valence, arousal) tuple in [-1, 1]
    """
    # Step 1: Probability sharpening to emphasize top emotion
    probs_array = np.array([
        emotion_probs.get('happy', 0.0),
        emotion_probs.get('sad', 0.0),
        emotion_probs.get('angry', 0.0),
        emotion_probs.get('fear', 0.0),
        emotion_probs.get('disgust', 0.0),
        emotion_probs.get('surprise', 0.0),
        emotion_probs.get('neutral', 0.0),
    ])
    
    # Apply sharpening: p' = p^sharp / Σ p^sharp
    if np.sum(probs_array) > 0:
        probs_sharpened = np.power(probs_array, sharp)
        probs_sharpened = probs_sharpened / np.sum(probs_sharpened)
    else:
        probs_sharpened = probs_array
    
    happy, sad, angry, fear, disgust, surprise, neutral = probs_sharpened
    
    # Step 2: Improved valence mapping (more balanced)
    # Increased positive weights and reduced negative weights for balance
    valence = (
        +1.2 * happy +         # 增强正面权重
        +0.4 * surprise +      # surprise 可以有正面语境
        +0.15 * neutral +      # neutral 给予正面偏置（+0.1 → +0.15）
        -0.85 * sad +          # 降低负面权重（-1.0 → -0.85）
        -0.65 * angry +        # 降低负面权重（-0.8 → -0.65）
        -0.55 * fear +         # 降低负面权重（-0.7 → -0.55）
        -0.55 * disgust         # 降低负面权重（-0.7 → -0.55）
    )
    
    # Step 3: Improved arousal mapping (more balanced)
    # 调整 arousal 的分布，避免过度集中在负区间
    arousal = (
        +0.7 * surprise +      # high energy
        +0.6 * angry +         # high energy  
        +0.6 * fear +          # high energy
        +0.5 * happy +         # increased (0.4 → 0.5)
        +0.3 * disgust +       # moderate (0.2 → 0.3)
        +0.1 * neutral +       # calm (中性点降低)
        -0.3 * sad             # 负向（低能量），从 0.1 → -0.3
    )
    
    # Step 4: Clamp to [-1, 1] range
    valence = np.clip(valence, -1.0, 1.0)
    arousal = np.clip(arousal, -1.0, 1.0)
    
    return float(valence), float(arousal)


def test_probs_to_va():
    """Simple test for the mapping function"""
    # Test case: mostly happy
    probs_happy = {
        'angry': 0.02,
        'disgust': 0.01,
        'fear': 0.05,
        'happy': 0.62,
        'sad': 0.03,
        'surprise': 0.21,
        'neutral': 0.06
    }
    
    v, a = probs_to_valence_arousal(probs_happy)
    print(f"Happy test: valence={v:.3f}, arousal={a:.3f}")
    assert v > 0.5, "Happy should have high positive valence"
    
    # Test case: mostly sad
    probs_sad = {
        'angry': 0.10,
        'disgust': 0.05,
        'fear': 0.05,
        'happy': 0.05,
        'sad': 0.70,
        'surprise': 0.02,
        'neutral': 0.03
    }
    
    v, a = probs_to_valence_arousal(probs_sad)
    print(f"Sad test: valence={v:.3f}, arousal={a:.3f}")
    assert v < 0, "Sad should have negative valence"
    
    print("Tests passed!")


if __name__ == "__main__":
    test_probs_to_va()

