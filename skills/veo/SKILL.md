---
name: veo
description: Generate videos using Google Veo 3.1. Use for video generation, animation, cinematic sequences, dialogue scenes, transitions, and any video creation task.
allowed-tools: Read, WebFetch
---

# Veo 3.1 - Video Generation Prompting Guide

Generate professional-quality videos using Google's Veo 3.1 model with complete audio capabilities.

## The 5-Part Prompt Formula

Structure your prompts using this formula for optimal control:

```
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
```

| Element | Description | Examples |
|---------|-------------|----------|
| **Cinematography** | Camera work and shot composition | Medium shot, crane shot, tracking shot |
| **Subject** | Main character or focal point | A tired office worker, three baby owls |
| **Action** | What the subject is doing | Rubbing his temples, huddling together |
| **Context** | Environment and background | In a cluttered office, on a moonlit branch |
| **Style & Ambiance** | Aesthetic, mood, lighting | Retro aesthetic, warm and cozy, cinematic |

### Example Prompt
```
Medium shot, a tired corporate worker, rubbing his temples in exhaustion,
in front of a bulky 1980s computer in a cluttered office late at night.
The scene is lit by harsh fluorescent overhead lights and the green glow
of the monochrome monitor. Retro aesthetic, shot as if on 1980s color film,
slightly grainy.
```

---

## Cinematography Language

The cinematography element is your most powerful tool for conveying tone and emotion.

### Camera Movement
| Movement | Effect | Use Case |
|----------|--------|----------|
| **Dolly shot** | Smooth horizontal movement | Following action, revealing space |
| **Tracking shot** | Camera follows subject | Action sequences, journeys |
| **Crane shot** | Vertical movement, often ascending | Reveals, epic moments |
| **Aerial view** | Bird's eye perspective | Establishing shots, scale |
| **Slow pan** | Gradual horizontal rotation | Scanning environments, tension |
| **POV shot** | Subject's perspective | Immersion, emotional connection |
| **Arc shot** | Camera circles subject | Drama, transformation moments |

**Crane Shot Example:**
```
Crane shot starting low on a lone hiker and ascending high above,
revealing they are standing on the edge of a colossal, mist-filled
canyon at sunrise, epic fantasy style, awe-inspiring, soft morning light.
```

### Shot Composition
| Shot | Description |
|------|-------------|
| **Wide shot** | Full environment, subject small in frame |
| **Medium shot** | Subject from waist up |
| **Close-up** | Face or object fills frame |
| **Extreme close-up** | Detail (eyes, hands, texture) |
| **Low angle** | Camera looks up at subject (power, drama) |
| **High angle** | Camera looks down (vulnerability, scale) |
| **Two-shot** | Two subjects in frame |

### Lens & Focus
| Technique | Effect |
|-----------|--------|
| **Shallow depth of field** | Subject sharp, background blurred (intimate, focus) |
| **Deep focus** | Everything sharp (epic, environmental) |
| **Wide-angle lens** | Expansive, slight distortion at edges |
| **Macro lens** | Extreme close-up of small details |
| **Soft focus** | Dreamy, romantic quality |

**Shallow DOF Example:**
```
Close-up with very shallow depth of field, a young woman's face,
looking out a bus window at the passing city lights with her reflection
faintly visible on the glass, inside a bus at night during a rainstorm,
melancholic mood with cool blue tones, moody, cinematic.
```

---

## Audio Direction

Veo 3.1 generates complete soundtracks from text instructions.

### Dialogue
Use quotation marks for specific speech:
```
A woman says, "We have to leave now."
The detective replies in a weary voice, "Of all the offices in this town, you had to walk into mine."
```

### Sound Effects (SFX)
Describe sounds with clarity:
```
SFX: thunder cracks in the distance
SFX: footsteps echo on marble floor
SFX: the rustle of dense leaves, distant exotic bird calls
```

### Ambient Noise
Define background soundscape:
```
Ambient noise: the quiet hum of a starship bridge
Ambient noise: gentle forest sounds with crickets
Ambient noise: busy city street with distant traffic
```

### Music
Describe musical elements:
```
SFX: A swelling, gentle orchestral score begins to play
Music: Soft piano melody, melancholic
Music: Upbeat electronic soundtrack builds
```

---

## Negative Prompts

To refine output, describe what to **exclude** using positive language:

| Instead of... | Use... |
|---------------|--------|
| "No buildings" | "A desolate landscape with no buildings or roads" |
| "No people" | "An empty street devoid of any pedestrians" |
| "No text" | "Clean frame without any text or labels" |

---

## Advanced Workflows

### Workflow 1: First and Last Frame (Dynamic Transitions)

Create controlled camera movements or transformations between two points.

**Step 1:** Generate starting frame with NanoBanana/Gemini
```
Medium shot of a female pop star singing passionately into a vintage
microphone. She is on a dark stage, lit by a single, dramatic spotlight
from the front. Photorealistic, cinematic.
```

**Step 2:** Generate ending frame
```
POV shot from behind the singer on stage, looking out at a large,
cheering crowd. The stage lights are bright, creating lens flare.
Energetic atmosphere.
```

**Step 3:** Animate with Veo (input both images)
```
The camera performs a smooth 180-degree arc shot, starting with the
front-facing view of the singer and circling around her to seamlessly
end on the POV shot from behind her on stage. The singer sings
"when you look me in the eyes, I can see a million stars."
```

---

### Workflow 2: Ingredients to Video (Character Consistency)

Create multi-shot scenes with consistent characters and dialogue.

**Step 1:** Generate reference images for:
- Character A (e.g., detective)
- Character B (e.g., mysterious woman)
- Setting (e.g., noir office)

**Step 2:** Use "Ingredients to Video" feature with references

**Shot 1:**
```
Using the provided images for the detective, the woman, and the office
setting, create a medium shot of the detective behind his desk. He looks
up at the woman and says in a weary voice, "Of all the offices in this
town, you had to walk into mine."
```

**Shot 2:**
```
Using the provided images for the detective, the woman, and the office
setting, create a shot focusing on the woman. A slight, mysterious smile
plays on her lips as she replies, "You were highly recommended."
```

---

### Workflow 3: Timestamp Prompting (Multi-Shot Sequences)

Direct complete multi-shot sequences with precise timing in a single generation.

**Format:** `[MM:SS-MM:SS] Shot description`

**Example:**
```
[00:00-00:02] Medium shot from behind a young female explorer with a
leather satchel and messy brown hair in a ponytail, as she pushes aside
a large jungle vine to reveal a hidden path.

[00:02-00:04] Reverse shot of the explorer's freckled face, her expression
filled with awe as she gazes upon ancient, moss-covered ruins in the
background. SFX: The rustle of dense leaves, distant exotic bird calls.

[00:04-00:06] Tracking shot following the explorer as she steps into the
clearing and runs her hand over the intricate carvings on a crumbling
stone wall. Emotion: Wonder and reverence.

[00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer
standing small in the center of the vast, forgotten temple complex,
half-swallowed by the jungle. SFX: A swelling, gentle orchestral score
begins to play.
```

---

## Style Reference with Images

When using style reference images:

1. **Generate reference images** using NanoBanana (Gemini 2.5 Flash Image or Gemini 3 Pro)
2. **Upload as style guide** when creating Veo prompt
3. **Reference the style** in your prompt:
   ```
   Maintaining the vibrant folk art style with saturated colors,
   needle-felted texture, and warm Coco-inspired lighting from
   the reference images...
   ```

---

## Quick Reference Templates

### Cinematic Scene
```
[Shot type] of [subject description], [action], [location/context].
[Lighting description]. [Style/mood]. [Audio: dialogue/SFX/ambient].
```

### Character Animation
```
[Shot type], [character description], [emotional state and action],
[environment]. Style: [aesthetic]. [Character says "dialogue"].
SFX: [sound effects]. Ambient: [background audio].
```

### Transition/Transformation
```
Starting with [initial shot description], the camera [movement type]
to reveal/transition to [ending shot description]. [Audio description].
```

### Multi-Shot Sequence
```
[00:00-00:XX] [Shot 1 description with audio]
[00:XX-00:XX] [Shot 2 description with audio]
[00:XX-00:XX] [Shot 3 description with audio]
...
```

---

## Tips for Best Results

1. **Be specific** - Vague prompts yield generic results
2. **Use cinematic language** - Camera terms give precise control
3. **Include audio direction** - Veo 3.1 generates complete soundtracks
4. **Layer details** - Subject + Action + Environment + Style + Sound
5. **Use reference images** - For style consistency across shots
6. **Timestamp for sequences** - Precise control over multi-shot videos
7. **Describe emotions** - "Expression filled with awe" not just "looking"
8. **Specify lighting** - Key to mood and atmosphere
