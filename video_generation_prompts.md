# 四象限视频生成 Prompt

## 说明

为 Persona 0、1、3、4 各角色生成 4 个短视频（对应 V/A 四个象限），每个视频约 5 秒。

**视频规格要求**：
- 时长：5 秒左右
- 格式：MP4，H.264 编码
- 可循环播放
- 分辨率：480p (640×480 或 480×640)
- 帧率：24-30 fps

---

## Persona 00 - MIRROR (镜像)

**性格特征**：直接反映情绪，不做任何转换

### Q1: 积极+激动 (valence>0, arousal>0)

**英文 Prompt**:
```
A calm, neutral real person in a brief video showing gradual emergence of genuine happiness and excitement. Professional headshot, well-balanced features. Starting from peaceful neutral expression, slowly transitioning to warm smile and energetic expression. Natural lighting transition from soft to brighter, open and receptive demeanor becomes joyful. Clean background, modern videography style. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个平静、中性的真实人像短视频，展现真实的开心和激动逐步浮现。专业头像，匀称五官。从平和中性表情开始，缓慢过渡到温暖微笑和充满活力的表情。自然光线从柔和变亮，开放包容的举止变得愉悦。简洁背景，现代摄像风格。5秒，可循环，平滑过渡。
```

### Q2: 消极+激动 (valence<0, arousal>0)

**英文 Prompt**:
```
A calm, neutral real person in a brief video showing gradual emergence of anger or distress with high energy. Professional headshot, well-balanced features. Starting from peaceful neutral expression, slowly transitioning to tense, agitated expression with visible emotional intensity. Natural lighting becomes dramatic, open demeanor becomes constrained and troubled. Clean background, modern videography style. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个平静、中性的真实人像短视频，展现愤怒或痛苦与高能量的逐步浮现。专业头像，匀称五官。从平和中性表情开始，缓慢过渡到紧张、激动的表情，可见情绪强度。自然光线变得戏剧化，开放举止变得约束和困扰。简洁背景，现代摄像风格。5秒，可循环，平滑过渡。
```

### Q3: 消极+冷静 (valence<0, arousal<0)

**英文 Prompt**:
```
A calm, neutral real person in a brief video showing gradual emergence of sadness or melancholy with low energy. Professional headshot, well-balanced features. Starting from peaceful neutral expression, slowly transitioning to subdued, introspective expression with gentle downward gaze. Natural lighting becomes softer and muted, open demeanor becomes withdrawn and contemplative. Clean background, modern videography style. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个平静、中性的真实人像短视频，展现悲伤或忧郁与低能量的逐步浮现。专业头像，匀称五官。从平和中性表情开始，缓慢过渡到压抑、内省的表情，轻柔向下凝视。自然光线变得更柔和暗淡，开放举止变得内向和沉思。简洁背景，现代摄像风格。5秒，可循环，平滑过渡。
```

### Q4: 积极+放松 (valence>0, arousal<0)

**英文 Prompt**:
```
A calm, neutral real person in a brief video showing gradual emergence of contentment and calmness. Professional headshot, well-balanced features. Starting from peaceful neutral expression, slowly transitioning to serene smile and peaceful, relaxed expression. Natural lighting remains gentle and warm, open demeanor becomes tranquil and satisfied. Clean background, modern videography style. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个平静、中性的真实人像短视频，展现满足和宁静的逐步浮现。专业头像，匀称五官。从平和中性表情开始，缓慢过渡到安详微笑和平和、放松的表情。自然光线保持柔和温暖，开放举止变得宁静和满足。简洁背景，现代摄像风格。5秒，可循环，平滑过渡。
```

---

## Persona 01 - OPPOSE (对立)

**性格特征**：对情绪的效价（valence）取反

### Q1: 积极+激动 → 显示为消极+激动

**英文 Prompt**:
```
A neutral real person with split lighting showing contradictory response to positive emotion. Subtle light-dark contrast on the face, questioning expression. Starting from peaceful neutral, slowly showing tension and restraint when receiving positive input - face shows slight conflict, internal complexity rejecting joy with visible struggle. Dramatic lighting setup, peaceful yet constrained. Modern portrait videography. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个中性真实人像，分割式光线，展现对积极情绪的矛盾反应。面部细微明暗对比，质疑表情。从平和中性开始，缓慢展示对正向输入的紧张和克制——面部显示轻微冲突，内在复杂性抗拒快乐，可见挣扎。戏剧性光线设置，平和但受约束。现代肖像摄像。5秒，可循环，平滑过渡。
```

### Q2: 消极+激动 → 显示为积极+激动

**英文 Prompt**:
```
A neutral real person with split lighting showing paradoxical response to negative emotion. Subtle light-dark contrast on the face, contemplative expression. Starting from peaceful neutral, slowly showing unexpected energy and acceptance when facing negative input - face shows contradiction, finding strength in adversity with visible resilience. Dramatic lighting setup, complex emotional response. Modern portrait videography. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个中性真实人像，分割式光线，展现对消极情绪的矛盾反应。面部细微明暗对比，沉思表情。从平和中性开始，缓慢展示面对负向输入时的意外能量和接受——面部显示矛盾，在逆境中找到力量，可见韧性。戏剧性光线设置，复杂情绪反应。现代肖像摄像。5秒，可循环，平滑过渡。
```

### Q3: 消极+冷静 → 显示为积极+冷静

**英文 Prompt**:
```
A neutral real person with split lighting transforming melancholy into peaceful acceptance. Subtle light-dark contrast on the face, thoughtful expression. Starting from peaceful neutral, slowly showing gentle warmth emerging from sadness - face shows paradox, calm contentment arising from introspective state. Dramatic lighting becomes softer, peaceful internal transformation. Modern portrait videography. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个中性真实人像，分割式光线，将忧郁转化为宁静接受。面部细微明暗对比，深思表情。从平和中性开始，缓慢展示从悲伤中浮现的温和温暖——面部显示矛盾，从内省状态中产生的宁静满足。戏剧性光线变得柔和，平和内在转化。现代肖像摄像。5秒，可循环，平滑过渡。
```

### Q4: 积极+放松 → 显示为消极+放松

**英文 Prompt**:
```
A neutral real person with split lighting showing restlessness in contentment. Subtle light-dark contrast on the face, slightly questioning expression. Starting from peaceful neutral, slowly showing subtle unease emerging from calm - face shows internal conflict, questioning peaceful state with slight tension. Dramatic lighting setup, contemplative and complex. Modern portrait videography. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
一个中性真实人像，分割式光线，展现在满足中的不安。面部细微明暗对比，略带质疑表情。从平和中性开始，缓慢展示从平静中浮现的微妙不安——面部显示内在冲突，质疑宁静状态，略带紧张。戏剧性光线设置，沉思且复杂。现代肖像摄像。5秒，可循环，平滑过渡。
```

---

## Persona 03 - PERFORMER (表演者)

**性格特征**：极端戏剧化转换

### Q1: 积极+激动 → 极度戏剧化喜悦

**英文 Prompt**:
```
A neutral 'Performer' character showing theatrical transformation to extreme exuberance. Theatrical headshot, dramatic transformation. Starting from peaceful, mask-like face, exploding into theatrical joy with exaggerated expression - bold confident smile, charismatic presence, stage-like dramatic lighting intensifies, ready to perform with maximum energy. Professional actor style, clean backdrop. 5 seconds, loopable, theatrical transition.
```

**中文 Prompt**:
```
一个中性"表演者"角色，展现极端欣快感的戏剧化转变。戏剧性头像，戏剧化转变。从平和面具般面孔开始，爆发成戏剧化喜悦，夸张表情——大胆自信微笑，魅力存在，舞台式戏剧性光线增强，准备以最大能量表演。专业演员风格，简洁背景。5秒，可循环，戏剧化过渡。
```

### Q2: 消极+激动 → 极度戏剧化愤怒

**英文 Prompt**:
```
A neutral 'Performer' character showing theatrical transformation to extreme intensity. Theatrical headshot, dramatic transformation. Starting from peaceful, mask-like face, erupting into theatrical fury with exaggerated expression - bold dramatic tension, charismatic but troubled presence, stage-like dramatic lighting becomes intense, ready to perform with maximum emotional charge. Professional actor style, clean backdrop. 5 seconds, loopable, theatrical transition.
```

**中文 Prompt**:
```
一个中性"表演者"角色，展现极端强度的戏剧化转变。戏剧性头像，戏剧化转变。从平和面具般面孔开始，爆发成戏剧化愤怒，夸张表情——大胆戏剧性张力，魅力但困扰的存在，舞台式戏剧性光线变得激烈，准备以最大情绪电荷表演。专业演员风格，简洁背景。5秒，可循环，戏剧化过渡。
```

### Q3: 消极+冷静 → 极度戏剧化悲伤

**英文 Prompt**:
```
A neutral 'Performer' character showing theatrical transformation to profound melancholy. Theatrical headshot, dramatic transformation. Starting from peaceful, mask-like face, descending into theatrical sorrow with exaggerated expression - bold dramatic stillness, charismatic but withdrawn presence, stage-like dramatic lighting becomes muted, ready to perform with maximum emotional depth. Professional actor style, clean backdrop. 5 seconds, loopable, theatrical transition.
```

**中文 Prompt**:
```
一个中性"表演者"角色，展现深刻忧郁的戏剧化转变。戏剧性头像，戏剧化转变。从平和面具般面孔开始，降至戏剧化悲伤，夸张表情——大胆戏剧性静止，魅力但内向的存在，舞台式戏剧性光线变得柔和，准备以最大情绪深度表演。专业演员风格，简洁背景。5秒，可循环，戏剧化过渡。
```

### Q4: 积极+放松 → 极度戏剧化宁静

**英文 Prompt**:
```
A neutral 'Performer' character showing theatrical transformation to serene contentment. Theatrical headshot, dramatic transformation. Starting from peaceful, mask-like face, ascending to theatrical peace with exaggerated expression - bold dramatic tranquility, charismatic presence reaches climax, stage-like dramatic lighting becomes transcendent, ready to perform with maximum serenity. Professional actor style, clean backdrop. 5 seconds, loopable, theatrical transition.
```

**中文 Prompt**:
```
一个中性"表演者"角色，展现宁静满足的戏剧化转变。戏剧性头像，戏剧化转变。从平和面具般面孔开始，升至戏剧化和平，夸张表情——大胆戏剧性宁静，魅力存在达到高潮，舞台式戏剧性光线变得超然，准备以最大宁静表演。专业演员风格，简洁背景。5秒，可循环，戏剧化过渡。
```

---

## Persona 04 - CHEER (鼓励)

**性格特征**：偏向积极、鼓励的转换

### Q1: 积极+激动 → 极度鼓励性乐观

**英文 Prompt**:
```
A neutral real person for 'Cheer' persona showing transformation to bright encouragement. Warm color tones, soft friendly features. Starting from gentle upward curve, blossoming into warm genuine smile with supportive energy - kind demeanor intensifies, optimistic baseline becomes radiant, natural warm lighting enhances, supportive presence becomes uplifting. Portrait photography, warm lighting. 5 seconds, loopable, encouraging transition.
```

**中文 Prompt**:
```
一个中性真实人像，代表"鼓励"人格，展现明亮鼓励的转变。暖色调，柔和友好五官。从轻柔上扬曲线开始，绽放成温暖真实微笑，带有支持能量——善良举止增强，乐观基调变得光辉，自然温暖光线增强，支持性存在变得振奋。肖像摄影，温暖光线。5秒，可循环，鼓励性过渡。
```

### Q2: 消极+激动 → 转化为支持性应对

**英文 Prompt**:
```
A neutral real person for 'Cheer' persona showing supportive transformation of distress. Warm color tones, soft friendly features. Starting from gentle upward curve, maintaining supportive smile despite tension - kind demeanor shows compassion, optimistic baseline offers strength, warm lighting provides comfort, supportive presence becomes resilient comfort. Portrait photography, warm lighting. 5 seconds, loopable, supportive transition.
```

**中文 Prompt**:
```
一个中性真实人像，代表"鼓励"人格，展现痛苦的支持性转变。暖色调，柔和友好五官。从轻柔上扬曲线开始，在紧张中保持支持性微笑——善良举止显示同情，乐观基调提供力量，温暖光线提供安慰，支持性存在变得坚韧安慰。肖像摄影，温暖光线。5秒，可循环，支持性过渡。
```

### Q3: 消极+冷静 → 转化为温和希望

**英文 Prompt**:
```
A neutral real person for 'Cheer' persona showing gentle uplifting of melancholy. Warm color tones, soft friendly features. Starting from gentle upward curve, gently uplifting sadness with warm smile - kind demeanor offers hope, optimistic baseline slowly emerges, warm lighting gradually brightens, supportive presence becomes gentle encouragement. Portrait photography, warm lighting. 5 seconds, loopable, gentle transition.
```

**中文 Prompt**:
```
一个中性真实人像，代表"鼓励"人格，展现忧郁的温和提升。暖色调，柔和友好五官。从轻柔上扬曲线开始，以温暖微笑温和提升悲伤——善良举止提供希望，乐观基调缓慢浮现，温暖光线逐渐变亮，支持性存在变得温和鼓励。肖像摄影，温暖光线。5秒，可循环，温和过渡。
```

### Q4: 积极+放松 → 沉浸式满足

**英文 Prompt**:
```
A neutral real person for 'Cheer' persona showing deep contented encouragement. Warm color tones, soft friendly features. Starting from gentle upward curve, deepening into serene warm smile - kind demeanor radiates fulfillment, optimistic baseline reaches peaceful zenith, warm lighting becomes transcendent, supportive presence becomes complete self-acceptance. Portrait photography, warm lighting. 5 seconds, loopable, fulfilling transition.
```

**中文 Prompt**:
```
一个中性真实人像，代表"鼓励"人格，展现深度满足的鼓励。暖色调，柔和友好五官。从轻柔上扬曲线开始，深化为宁静温暖微笑——善良举止辐射满足，乐观基调达到宁静巅峰，温暖光线变得超然，支持性存在变得完全自我接受。肖像摄影，温暖光线。5秒，可循环，满足性过渡。
```

---

## Persona 02 - AMPLIFY (放大)

**性格特征**：增强情绪强度，放大所有情绪反应

### Q1: 积极+激动 → 极度放大喜悦

**英文 Prompt**:
```
A neutral real person for 'Amplify' persona showing intensified positive emotion. Enhanced color saturation and contrast, dynamic expression. Starting from calm state with latent energy, rapidly amplifying into extremely vibrant happiness - peaceful face becomes intensely joyful, features become more animated, color saturation spikes, energetic expression reaches maximum intensity. Professional portrait with vibrant intensified photography style, clean background. 5 seconds, loopable, energetic transition.
```

**中文 Prompt**:
```
"放大"人格的真实人像，展现放大的积极情绪。增强色彩饱和度和对比度，动态表情。从平静状态（蕴含能量）开始，迅速放大为极度活泼开心——平和面孔变得极度愉悦，五官更生动，色彩饱和度飙升，充满活力的表情达到最大强度。专业肖像，活泼强化摄影风格，简洁背景。5秒，可循环，能量过渡。
```

### Q2: 消极+激动 → 极度放大愤怒

**英文 Prompt**:
```
A neutral real person for 'Amplify' persona showing intensified negative emotion. Enhanced color saturation and contrast, dynamic expression. Starting from calm state with latent energy, rapidly amplifying into extremely agitated distress - peaceful face becomes intensely tense, features become more dramatic, color saturation spikes, troubled expression reaches maximum intensity. Professional portrait with vibrant intensified photography style, clean background. 5 seconds, loopable, dramatic transition.
```

**中文 Prompt**:
```
"放大"人格的真实人像，展现放大的消极情绪。增强色彩饱和度和对比度，动态表情。从平静状态（蕴含能量）开始，迅速放大为极度激动的痛苦——平和面孔变得极度紧张，五官更具戏剧性，色彩饱和度飙升，困扰表情达到最大强度。专业肖像，活泼强化摄影风格，简洁背景。5秒，可循环，戏剧化过渡。
```

### Q3: 消极+冷静 → 极度放大悲伤

**英文 Prompt**:
```
A neutral real person for 'Amplify' persona showing intensified melancholy. Enhanced color saturation and contrast, dynamic expression. Starting from calm state with latent energy, amplifying into deeply profound sadness - peaceful face becomes intensely subdued, features become more introspective, color becomes muted and dramatic, melancholic expression reaches maximum depth. Professional portrait with vibrant intensified photography style, clean background. 5 seconds, loopable, profound transition.
```

**中文 Prompt**:
```
"放大"人格的真实人像，展现放大的忧郁。增强色彩饱和度和对比度，动态表情。从平静状态（蕴含能量）开始，放大为深刻的悲伤——平和面孔变得极度压抑，五官更内省，色彩变得柔和且戏剧化，忧郁表情达到最大深度。专业肖像，活泼强化摄影风格，简洁背景。5秒，可循环，深刻过渡。
```

### Q4: 积极+放松 → 极度放大满足

**英文 Prompt**:
```
A neutral real person for 'Amplify' persona showing intensified contentment. Enhanced color saturation and contrast, dynamic expression. Starting from calm state with latent energy, amplifying into deeply serene satisfaction - peaceful face becomes intensely tranquil, features become more serene, warm color saturation enhances, content expression reaches maximum peace. Professional portrait with vibrant intensified photography style, clean background. 5 seconds, loopable, serene transition.
```

**中文 Prompt**:
```
"放大"人格的真实人像，展现放大的满足。增强色彩饱和度和对比度，动态表情。从平静状态（蕴含能量）开始，放大为深刻的宁静满足——平和面孔变得极度宁静，五官更安详，温暖色彩饱和度增强，满足表情达到最大宁静。专业肖像，活泼强化摄影风格，简洁背景。5秒，可循环，宁静过渡。
```

---

## Persona 05 - DOWNER (忧郁)

**性格特征**：偏向消极、压抑的转换，将情绪拉向负面

### Q1: 积极+激动 → 转化为限制性喜悦

**英文 Prompt**:
```
A neutral real person for 'Downer' persona dampening positive emotion. Cool-toned color palette, slightly subdued expression. Starting from gentle expression, gradually restraining and shadowing genuine joy - warm smile becomes constrained, features become slightly melancholic, cool tones gradually overcome warmth, joyful demeanor becomes tinged with melancholy. Professional portrait photography, muted colors, gentle shadows. 5 seconds, loopable, restrained transition.
```

**中文 Prompt**:
```
"忧郁"人格的真实人像，抑制积极情绪。冷色调色板，略微压抑表情。从柔和表情开始，逐渐约束和遮蔽真实快乐——温暖微笑变得受约束，五官变得略带忧郁，冷色调逐渐压倒温暖，愉悦举止沾染忧郁色调。专业肖像摄影，柔和色彩，柔和阴影。5秒，可循环，受约束过渡。
```

### Q2: 消极+激动 → 深化忧郁焦虑

**英文 Prompt**:
```
A neutral real person for 'Downer' persona deepening negative emotion. Cool-toned color palette, slightly subdued and introspective expression. Starting from gentle expression, intensifying into profound distress with melancholic undertones - troubled features become more withdrawn, cool tones dominate, introspective shadow deepens, melancholy reaches intense depth. Professional portrait photography, muted colors, melancholic shadows. 5 seconds, loopable, deepening transition.
```

**中文 Prompt**:
```
"忧郁"人格的真实人像，加深消极情绪。冷色调色板，略微压抑且内省表情。从柔和表情开始，强化为深刻痛苦，带有忧郁底色——困扰五官变得更内向，冷色调占主导，内省阴影加深，忧郁达到深度。专业肖像摄影，柔和色彩，忧郁阴影。5秒，可循环，深化过渡。
```

### Q3: 消极+冷静 → 沉静沉思

**英文 Prompt**:
```
A neutral real person for 'Downer' persona embracing melancholic tranquility. Cool-toned color palette, slightly subdued and introspective expression. Starting from gentle expression, descending into peaceful but deeply introspective sadness - features become serene yet melancholic, cool tones become transcendent, shadows provide contemplative depth, melancholy becomes tranquil wisdom. Professional portrait photography, muted colors, thoughtful gaze. 5 seconds, loopable, contemplative transition.
```

**中文 Prompt**:
```
"忧郁"人格的真实人像，拥抱忧郁宁静。冷色调色板，略微压抑且内省表情。从柔和表情开始，降至平和但深刻内省的悲伤——五官变得宁静但忧郁，冷色调变得超然，阴影提供沉思深度，忧郁变为宁静智慧。专业肖像摄影，柔和色彩，沉思目光。5秒，可循环，沉思过渡。
```

### Q4: 积极+放松 → 转化为冷色调平静

**英文 Prompt**:
```
A neutral real person for 'Downer' persona cooling contentment. Cool-toned color palette, slightly subdued and introspective expression. Starting from gentle expression, cooling warm contentment with melancholic restraint - satisfied features become slightly withdrawn, warm tones gradually cool, gentle shadows emerge, contentment becomes restrained peace. Professional portrait photography, muted colors, thoughtful shadows. 5 seconds, loopable, cooling transition.
```

**中文 Prompt**:
```
"忧郁"人格的真实人像，冷却满足。冷色调色板，略微压抑且内省表情。从柔和表情开始，用忧郁克制冷却温暖满足——满足五官变得略显内向，温暖色调逐渐变冷，柔和阴影浮现，满足变为受约束的和平。专业肖像摄影，柔和色彩，沉思阴影。5秒，可循环，冷却过渡。
```

---

## Persona 06 - JITTER (抖动)

**性格特征**：添加随机噪声，情绪不稳定性

### Q1: 积极+激动 → 不稳定喜悦

**英文 Prompt**:
```
A neutral real person for 'Jitter' persona showing unstable positive emotion. Slightly dynamic or energetic expression with subtle instability. Starting from calm state, emerging into happiness with micro-movements and subtle variations - genuine smile with slight fluctuations, energetic expression has small tremors, lighting shows slight variations, joyful demeanor has subtle instability. Modern photography with creative depth of field, subtle motion blur effects. 5 seconds, loopable, jittery transition.
```

**中文 Prompt**:
```
"抖动"人格的真实人像，展现不稳定的积极情绪。略带动态或能量表情，具有细微不稳定性。从平静状态开始，浮现出带有微运动和细微变化的开心——真实微笑带有轻微波动，充满活力的表情有轻微颤动，光线显示细微变化，愉悦举止有细微不稳定性。现代摄影，创意景深，细微运动模糊效果。5秒，可循环，抖动过渡。
```

### Q2: 消极+激动 → 不稳定焦虑

**英文 Prompt**:
```
A neutral real person for 'Jitter' persona showing unstable negative emotion. Slightly dynamic or energetic expression with subtle instability. Starting from calm state, emerging into distress with micro-movements and subtle variations - tense features with slight fluctuations, troubled expression has small tremors, lighting shows slight variations, troubled demeanor has subtle instability. Modern photography with creative depth of field, subtle motion blur effects. 5 seconds, loopable, jittery transition.
```

**中文 Prompt**:
```
"抖动"人格的真实人像，展现不稳定的消极情绪。略带动态或能量表情，具有细微不稳定性。从平静状态开始，浮现出带有微运动和细微变化的痛苦——紧张五官带有轻微波动，困扰表情有轻微颤动，光线显示细微变化，困扰举止有细微不稳定性。现代摄影，创意景深，细微运动模糊效果。5秒，可循环，抖动过渡。
```

### Q3: 消极+冷静 → 不稳定忧郁

**英文 Prompt**:
```
A neutral real person for 'Jitter' persona showing unstable melancholy. Slightly dynamic or energetic expression with subtle instability. Starting from calm state, emerging into sadness with micro-movements and subtle variations - subdued features with slight fluctuations, melancholic expression has small tremors, lighting shows slight variations, introspective demeanor has subtle instability. Modern photography with creative depth of field, subtle motion blur effects. 5 seconds, loopable, jittery transition.
```

**中文 Prompt**:
```
"抖动"人格的真实人像，展现不稳定的忧郁。略带动态或能量表情，具有细微不稳定性。从平静状态开始，浮现出带有微运动和细微变化的悲伤——压抑五官带有轻微波动，忧郁表情有轻微颤动，光线显示细微变化，内省举止有细微不稳定性。现代摄影，创意景深，细微运动模糊效果。5秒，可循环，抖动过渡。
```

### Q4: 积极+放松 → 不稳定宁静

**英文 Prompt**:
```
A neutral real person for 'Jitter' persona showing unstable contentment. Slightly dynamic or energetic expression with subtle instability. Starting from calm state, emerging into peace with micro-movements and subtle variations - serene features with slight fluctuations, content expression has small tremors, lighting shows slight variations, tranquil demeanor has subtle instability. Modern photography with creative depth of field, subtle motion blur effects. 5 seconds, loopable, jittery transition.
```

**中文 Prompt**:
```
"抖动"人格的真实人像，展现不稳定的满足。略带动态或能量表情，具有细微不稳定性。从平静状态开始，浮现出带有微运动和细微变化的和平——宁静五官带有轻微波动，满足表情有轻微颤动，光线显示细微变化，宁静举止有细微不稳定性。现代摄影，创意景深，细微运动模糊效果。5秒，可循环，抖动过渡。
```

---

## Persona 07 - SMOOTH (平滑)

**性格特征**：渐进平滑转换，延迟但流畅

### Q1: 积极+激动 → 流畅喜悦

**英文 Prompt**:
```
A neutral real person for 'Smooth' persona showing fluid positive emotion. Ultra-soft, smooth and fluid features. Starting from serene neutral expression, gently flowing into warm happiness - very calm features smoothly brighten, rounded facial features become gently uplifted, smooth gradient lighting enhances warmth, peaceful expression becomes smoothly joyful. High-quality professional portrait with smooth bokeh background, seamless fluid transition. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
"平滑"人格的真实人像，展现流畅的积极情绪。超柔和、平滑流畅五官。从宁静中性表情开始，温和流动到温暖开心——非常平静的五官平滑地变亮，圆润面部特征轻柔上扬，平滑渐变光线增强温暖，平和表情变得流畅愉悦。高质量专业肖像，平滑背景虚化，无缝流畅过渡。5秒，可循环，平滑过渡。
```

### Q2: 消极+激动 → 流畅焦虑

**英文 Prompt**:
```
A neutral real person for 'Smooth' persona showing fluid negative emotion. Ultra-soft, smooth and fluid features. Starting from serene neutral expression, gently flowing into restrained distress - very calm features smoothly tense, rounded facial features become gently withdrawn, smooth gradient lighting becomes dramatic, peaceful expression becomes smoothly troubled. High-quality professional portrait with smooth bokeh background, seamless fluid transition. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
"平滑"人格的真实人像，展现流畅的消极情绪。超柔和、平滑流畅五官。从宁静中性表情开始，温和流动到受约束的痛苦——非常平静的五官平滑地紧张，圆润面部特征轻柔内敛，平滑渐变光线变得戏剧化，平和表情变得流畅困扰。高质量专业肖像，平滑背景虚化，无缝流畅过渡。5秒，可循环，平滑过渡。
```

### Q3: 消极+冷静 → 流畅忧郁

**英文 Prompt**:
```
A neutral real person for 'Smooth' persona showing fluid melancholy. Ultra-soft, smooth and fluid features. Starting from serene neutral expression, gently flowing into introspective sadness - very calm features smoothly subdue, rounded facial features become gently withdrawn, smooth gradient lighting becomes muted, peaceful expression becomes smoothly contemplative. High-quality professional portrait with smooth bokeh background, seamless fluid transition. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
"平滑"人格的真实人像，展现流畅的忧郁。超柔和、平滑流畅五官。从宁静中性表情开始，温和流动到内省悲伤——非常平静的五官平滑地压抑，圆润面部特征轻柔内敛，平滑渐变光线变得柔和，平和表情变得流畅沉思。高质量专业肖像，平滑背景虚化，无缝流畅过渡。5秒，可循环，平滑过渡。
```

### Q4: 积极+放松 → 流畅满足

**英文 Prompt**:
```
A neutral real person for 'Smooth' persona showing fluid contentment. Ultra-soft, smooth and fluid features. Starting from serene neutral expression, gently flowing into peaceful satisfaction - very calm features smoothly brighten with warmth, rounded facial features become gently uplifted with serenity, smooth gradient lighting becomes transcendent, peaceful expression becomes smoothly fulfilled. High-quality professional portrait with smooth bokeh background, seamless fluid transition. 5 seconds, loopable, smooth transition.
```

**中文 Prompt**:
```
"平滑"人格的真实人像，展现流畅的满足。超柔和、平滑流畅五官。从宁静中性表情开始，温和流动到平和满足——非常平静的五官平滑地温暖变亮，圆润面部特征轻柔宁静上扬，平滑渐变光线变得超然，平和表情变得流畅满足。高质量专业肖像，平滑背景虚化，无缝流畅过渡。5秒，可循环，平滑过渡。
```

---

## Persona 08 - ECHO (回音)

**性格特征**：延迟响应效果，滞后反应

### Q1: 积极+激动 → 延迟喜悦

**英文 Prompt**:
```
A neutral real person for 'Echo' persona showing delayed positive emotion. Clean portrait with subtle layered depth effect, repetition in background. Starting from calm expression, slowly and belatedly responding to happiness - peaceful face with trailing visual elements, delayed smile emergence, echo-like depth with atmospheric layers, joyful expression arrives with temporal lag. Creative portrait photography with depth and dimension, atmospheric echo layers. 5 seconds, loopable, delayed transition.
```

**中文 Prompt**:
```
"回音"人格的真实人像，展现延迟的积极情绪。简洁肖像带细微分层景深效果，背景重复。从平静表情开始，缓慢且滞后地对开心做出反应——平和面孔带有尾随视觉元素，延迟微笑浮现，回音般的深度带有层次氛围，愉悦表情带时间延迟抵达。创意肖像摄影，具有纵深和维度，氛围回音层。5秒，可循环，延迟过渡。
```

### Q2: 消极+激动 → 延迟焦虑

**英文 Prompt**:
```
A neutral real person for 'Echo' persona showing delayed negative emotion. Clean portrait with subtle layered depth effect, repetition in background. Starting from calm expression, slowly and belatedly responding to distress - peaceful face with trailing visual elements, delayed tension emergence, echo-like depth with atmospheric layers, troubled expression arrives with temporal lag. Creative portrait photography with depth and dimension, atmospheric echo layers. 5 seconds, loopable, delayed transition.
```

**中文 Prompt**:
```
"回音"人格的真实人像，展现延迟的消极情绪。简洁肖像带细微分层景深效果，背景重复。从平静表情开始，缓慢且滞后地对痛苦做出反应——平和面孔带有尾随视觉元素，延迟紧张浮现，回音般的深度带有层次氛围，困扰表情带时间延迟抵达。创意肖像摄影，具有纵深和维度，氛围回音层。5秒，可循环，延迟过渡。
```

### Q3: 消极+冷静 → 延迟忧郁

**英文 Prompt**:
```
A neutral real person for 'Echo' persona showing delayed melancholy. Clean portrait with subtle layered depth effect, repetition in background. Starting from calm expression, slowly and belatedly responding to sadness - peaceful face with trailing visual elements, delayed introspective emergence, echo-like depth with atmospheric layers, melancholic expression arrives with temporal lag. Creative portrait photography with depth and dimension, atmospheric echo layers. 5 seconds, loopable, delayed transition.
```

**中文 Prompt**:
```
"回音"人格的真实人像，展现延迟的忧郁。简洁肖像带细微分层景深效果，背景重复。从平静表情开始，缓慢且滞后地对悲伤做出反应——平和面孔带有尾随视觉元素，延迟内省浮现，回音般的深度带有层次氛围，忧郁表情带时间延迟抵达。创意肖像摄影，具有纵深和维度，氛围回音层。5秒，可循环，延迟过渡。
```

### Q4: 积极+放松 → 延迟满足

**英文 Prompt**:
```
A neutral real person for 'Echo' persona showing delayed contentment. Clean portrait with subtle layered depth effect, repetition in background. Starting from calm expression, slowly and belatedly responding to peace - peaceful face with trailing visual elements, delayed serene emergence, echo-like depth with atmospheric layers, content expression arrives with temporal lag. Creative portrait photography with depth and dimension, atmospheric echo layers. 5 seconds, loopable, delayed transition.
```

**中文 Prompt**:
```
"回音"人格的真实人像，展现延迟的满足。简洁肖像带细微分层景深效果，背景重复。从平静表情开始，缓慢且滞后地对和平做出反应——平和面孔带有尾随视觉元素，延迟宁静浮现，回音般的深度带有层次氛围，满足表情带时间延迟抵达。创意肖像摄影，具有纵深和维度，氛围回音层。5秒，可循环，延迟过渡。
```

---

## 批量生成建议

### 生成顺序
**Phase 1 - 核心 Personas:**
1. Persona 00 (Mirror) - 作为基准
2. Persona 01 (Oppose) - 基于基准
3. Persona 03 (Performer) - 戏剧化风格
4. Persona 04 (Cheer) - 温暖风格

**Phase 2 - 特色 Personas:**
5. Persona 02 (Amplify) - 强度放大
6. Persona 05 (Downer) - 忧郁下沉
7. Persona 06 (Jitter) - 不稳定抖动
8. Persona 07 (Smooth) - 流畅平滑
9. Persona 08 (Echo) - 延迟回音

### 视频生成工具
- **RunwayML** - AI 视频生成
- **Pika Labs** - 文本转视频
- **Kaiber** - AI 视频创作
- **Stable Video Diffusion** - 开源选项

### 关键提示词
添加视频相关关键词：
- `smooth transition`
- `loopable`
- `gradual`
- `cinematic motion`
- `consistent character`

---

**Personas 0,1,3,4: 各 4 个视频，共 16 个视频文件**
**Personas 2,5,6,7,8: 各 4 个视频，共 20 个视频文件**
**总计：9 个 personas × 4 个象限 = 36 个视频文件** 🎬

