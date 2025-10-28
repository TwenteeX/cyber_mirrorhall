# 九个人格初始图像生成 Prompt

## 说明
这些 prompt 用于生成九个人格的**中性状态**初始图像，作为系统的基础角色形象。

**图像规格要求**：
- 分辨率：480P (640x480 或 480x640)
- 格式：PNG
- 风格：真实人像照片，自然光线
- 情绪状态：中性/平静

---

## Persona 00 - MIRROR (镜像)

**英文 Prompt**:
```
A calm, neutral real person portrait representing 'Mirror' persona. Professional headshot, well-balanced and symmetrical features. Soft natural lighting, peaceful expression, open and receptive demeanor. Clean background, modern photography style. 
```

**中文 Prompt**:
```
一个平静、中性的真实人像照片，代表"镜像"人格。专业头像照，匀称且对称的五官。柔和自然光线，平和表情，开放而包容的举止。简洁背景，现代摄影风格。
```

**性格特征**：直接反映情绪，不做任何转换

---

## Persona 01 - OPPOSE (对立)

**英文 Prompt**:
```
A neutral real person portrait representing 'Oppose' persona. Split lighting with slight light-dark contrast, creating subtle duality in the face. Slightly questioning or contemplative expression. Peaceful yet with underlying complexity. Modern portrait photography, dramatic lighting setup.
```

**中文 Prompt**:
```
一个中性的真实人像，代表"对立"人格。分割式光线，轻微明暗对比，在面部创造细微的对立感。略带质疑或沉思的表情。平和但具内在复杂性。现代肖像摄影，戏剧性光线设置。
```

**性格特征**：对情绪的效价（valence）取反

---

## Persona 02 - AMPLIFY (放大)

**英文 Prompt**:
```
A neutral real person portrait for 'Amplify' persona. Enhanced color saturation and contrast, dynamic expression even in calm state. Peaceful face with latent energy and intensity. Professional portrait with vibrant, intensified photography style. Clean background.
```

**中文 Prompt**:
```
"放大"人格的真实中性人像。增强的色彩饱和度和对比度，平静状态下也具动态表情。平和的面部带有潜在能量和强度。专业肖像，活泼强化摄影风格。简洁背景。
```

**性格特征**：增强情绪强度

---

## Persona 03 - PERFORMER (表演者)

**英文 Prompt**:
```
A neutral real person portrait for 'Performer' persona. Theatrical headshot with expressive but controlled pose. Stage-like dramatic lighting, bold and confident expression. Peaceful face ready to perform, charismatic presence. Professional actor portrait style, clean backdrop.
```

**中文 Prompt**:
```
"表演者"人格的真实中性人像。戏剧性头像照，表情丰富但姿势受控。舞台式戏剧性光线，大胆自信的表情。平和的面部准备表演，具有魅力。专业演员肖像风格，简洁背景。
```

**性格特征**：极端戏剧化转换

---

## Persona 04 - CHEER (鼓励)

**英文 Prompt**:
```
A neutral real person portrait for 'Cheer' persona. Slight warm smile or gentle upward expression. Warm color tones in the photograph, soft and friendly features. Supportive and kind demeanor. Optimistic baseline expression. Natural portrait photography, warm lighting.
```

**中文 Prompt**:
```
"鼓励"人格的真实中性人像。略带温暖微笑或轻柔上扬表情。照片采用暖色调，柔和友好五官。支持性且善良举止。乐观基调表情。自然肖像摄影，温暖光线。
```

**性格特征**：偏向积极、鼓励的转换

---

## Persona 05 - DOWNER (忧郁)

**英文 Prompt**:
```
A neutral real person portrait for 'Downer' persona. Cool-toned color palette in the photo, slightly subdued and introspective expression. Melancholic undertones while maintaining calm demeanor. Soft natural shadows, thoughtful gaze. Professional portrait photography, muted colors.
```

**中文 Prompt**:
```
"忧郁"人格的真实中性人像。照片采用冷色调色板，略微压抑且内省表情。保持平静举止的同时带有忧郁底色。柔和自然阴影，沉思目光。专业肖像摄影，色彩柔和。
```

**性格特征**：偏向消极、压抑的转换

---

## Persona 06 - JITTER (抖动)

**英文 Prompt**:
```
A neutral real person portrait for 'Jitter' persona. Slightly dynamic or energetic expression while maintaining calm. Natural portrait with subtle movement, perhaps slight motion blur or layered focus effects. Energetic but controlled expression. Modern photography with creative depth of field.
```

**中文 Prompt**:
```
"抖动"人格的真实中性人像。略带动态或能量表情，同时保持平静。自然肖像带细微运动感，可能有轻微运动模糊或分层聚焦效果。能量但受控的表情。现代摄影，创意景深。
```

**性格特征**：添加随机噪声

---

## Persona 07 - SMOOTH (平滑)

**英文 Prompt**:
```
A neutral real person portrait for 'Smooth' persona. Ultra-soft, smooth and fluid features. Very calm and peaceful expression with soft, rounded facial features. Gentle gradient lighting for seamless look. Tranquil and serene appearance. High-quality professional portrait with smooth bokeh background.
```

**中文 Prompt**:
```
"平滑"人格的真实中性人像。超柔和、平滑流畅五官。非常平静和平和的表情，柔和圆润面部特征。柔和渐变光线呈现无缝感。宁静祥和外观。高质量专业肖像，平滑背景虚化。
```

**性格特征**：渐进平滑转换

---

## Persona 08 - ECHO (回音)

**英文 Prompt**:
```
A neutral real person portrait for 'Echo' persona. Clean portrait with subtle layered depth effect, perhaps with slight repetition or reflection in the background. Calm expression with delayed visual elements creating echo-like depth. Peaceful face with atmospheric layers. Creative portrait photography with depth and dimension.
```

**中文 Prompt**:
```
"回音"人格的真实中性人像。简洁肖像带细微分层景深效果，背景可能带有轻微重复或反射。平静表情，延迟视觉元素营造回音般的深度。平和面孔与层次氛围。创意肖像摄影，具有纵深和维度。
```

**性格特征**：延迟响应效果

---

## 统一生成建议

### 批量生成参数：
- **模型**：Midjourney / DALL-E 3 / Stable Diffusion
- **宽高比**：4:3 或 3:4
- **风格关键词**：`professional portrait photography`, `neutral expression`, `real person headshot`, `natural lighting`
- **质量控制**：`high quality`, `clean composition`, `sharp focus`, `well-lit`

### 可选统一调整：
- 添加相同的边框或背景色
- 统一的光照方向
- 相似的面部角度/朝向
- 一致的色彩饱和度

### 生成顺序建议：
1. 先生成 Persona 00 (Mirror) 作为基准风格
2. 基于基准调整其他人格
3. 确保视觉连贯性（同一主题系列）

---

## 快速复制粘贴版（真实人像）

```
Persona 00: A calm, neutral real person portrait representing 'Mirror' persona. Professional headshot, well-balanced and symmetrical features. Soft natural lighting, peaceful expression, open and receptive demeanor. Clean background, modern photography style.

Persona 01: A neutral real person portrait representing 'Oppose' persona. Split lighting with slight light-dark contrast, creating subtle duality in the face. Slightly questioning or contemplative expression. Peaceful yet with underlying complexity. Modern portrait photography, dramatic lighting setup.

Persona 02: A neutral real person portrait for 'Amplify' persona. Enhanced color saturation and contrast, dynamic expression even in calm state. Peaceful face with latent energy and intensity. Professional portrait with vibrant, intensified photography style. Clean background.

Persona 03: A neutral real person portrait for 'Performer' persona. Theatrical headshot with expressive but controlled pose. Stage-like dramatic lighting, bold and confident expression. Peaceful face ready to perform, charismatic presence. Professional actor portrait style, clean backdrop.

Persona 04: A neutral real person portrait for 'Cheer' persona. Slight warm smile or gentle upward expression. Warm color tones in the photograph, soft and friendly features. Supportive and kind demeanor. Optimistic baseline expression. Natural portrait photography, warm lighting.

Persona 05: A neutral real person portrait for 'Downer' persona. Cool-toned color palette in the photo, slightly subdued and introspective expression. Melancholic undertones while maintaining calm demeanor. Soft natural shadows, thoughtful gaze. Professional portrait photography, muted colors.

Persona 06: A neutral real person portrait for 'Jitter' persona. Slightly dynamic or energetic expression while maintaining calm. Natural portrait with subtle movement, perhaps slight motion blur or layered focus effects. Energetic but controlled expression. Modern photography with creative depth of field.

Persona 07: A neutral real person portrait for 'Smooth' persona. Ultra-soft, smooth and fluid features. Very calm and peaceful expression with soft, rounded facial features. Gentle gradient lighting for seamless look. Tranquil and serene appearance. High-quality professional portrait with smooth bokeh background.

Persona 08: A neutral real person portrait for 'Echo' persona. Clean portrait with subtle layered depth effect, perhaps with slight repetition or reflection in the background. Calm expression with delayed visual elements creating echo-like depth. Peaceful face with atmospheric layers. Creative portrait photography with depth and dimension.
```

---

## 使用建议

1. **一次性生成**：将所有 9 个 prompt 同时提交，确保风格统一
2. **迭代优化**：根据第一个结果调整参数
3. **格式统一**：所有人格图像使用相同尺寸和格式
4. **命名规范**：保存为 `persona_00_neutral.png` 到 `persona_08_neutral.png`

完成后，这些图像可以作为系统的基础资产，未来可以据此生成四种不同情绪版本（Q1-Q4）。

