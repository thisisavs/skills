---
name: nanobanana
description: Generate and edit images using Google Gemini (NanoBanana Pro). Use when asked to generate images, create artwork, illustrations, concept art, edit images, style transfer, storyboards, infographics, or any visual creation task.
allowed-tools: Bash(python:*), Read
---

# NanoBanana Pro - Google Gemini Image Generation

Generate professional-quality images using Google's Gemini 3 Pro Image model.

> **Key Insight**: Nano-Banana Pro is a "Thinking" model. It doesn't just match keywords; it understands intent, physics, and composition. Stop using "tag soups" and start acting like a **Creative Director**.

## Quick Start

```bash
python ~/.claude/skills/nanobanana/scripts/generate.py "your prompt here"
```

---

## The Golden Rules of Prompting

### 1. Edit, Don't Re-roll
If an image is 80% correct, don't regenerate from scratch. Ask for the specific change:
> "That's great, but change the lighting to sunset and make the text neon blue."

### 2. Use Natural Language & Full Sentences
Talk to the model as if you were briefing a human artist.

| Bad | Good |
|-----|------|
| "Cool car, neon, city, night, 8k" | "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. The neon signs reflect off the wet pavement and the car's metallic chassis." |

### 3. Be Specific and Descriptive
Vague prompts yield generic results. Define:
- **Subject**: Not "a woman" → "a sophisticated elderly woman wearing a vintage Chanel-style suit"
- **Materiality**: "Matte finish," "brushed steel," "soft velvet," "crumpled paper"
- **Setting**: Location, time of day, weather
- **Lighting**: "soft golden hour light," "dramatic shadows," "neon glow"
- **Mood**: "serene," "tense," "whimsical"

### 4. Provide Context (The "Why" or "For Whom")
Context helps the model make logical artistic decisions:
> "Create an image of a sandwich **for a Brazilian high-end gourmet cookbook**."

The model will infer professional plating, shallow depth of field, and perfect lighting.

---

## Models

| Model | ID | Best For |
|-------|-----|----------|
| **Pro** (default) | `gemini-3-pro-image-preview` | Professional quality, complex prompts, 4K, thinking mode |
| **Flash** | `gemini-2.5-flash-image` | Speed, high-volume, quick iterations (1024px max) |

---

## Usage

```bash
python ~/.claude/skills/nanobanana/scripts/generate.py "prompt" [options]
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output` | Output file path | Auto: `generated_images/nano_TIMESTAMP.{ext}` |
| `-a, --aspect` | Aspect ratio | `16:9` |
| `-r, --resolution` | Resolution (Pro only) | `2K` |
| `-m, --model` | Model: `pro` or `flash` | `pro` |
| `-i, --input` | Input image for editing/style transfer | None |
| `--search` | Enable Google Search grounding | False |

### Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| `1:1` | Square (social media, icons) |
| `3:4` | Portrait (book covers) |
| `4:3` | Standard screen |
| **`16:9`** | **Widescreen/cinematic (DEFAULT)** |
| `9:16` | Vertical video/phone |
| `21:9` | Ultra-wide/cinematic |

### Resolutions (Pro Model Only)

| Resolution | 16:9 Dimensions | Notes |
|------------|-----------------|-------|
| `1K` | 1376x768 | Faster |
| **`2K`** | **2752x1536** | **Default, recommended** |
| `4K` | 5504x3072 | Highest quality, best for textures |

**Important:** Resolution must be uppercase (`1K`, `2K`, `4K`)!

---

## Professional Capabilities

### 1. Text Rendering & Infographics
Nano-Banana Pro has SOTA text rendering capabilities.

**Best Practices:**
- **Compression**: Ask to "compress" dense text or PDFs into visual aids
- **Style**: Specify "polished editorial," "technical diagram," or "hand-drawn whiteboard"
- **Quotes**: Clearly specify text you want rendered in quotes

**Example:**
```
"Generate a clean, modern infographic summarizing the key financial highlights
from this earnings report. Include charts for 'Revenue Growth' and 'Net Income',
and highlight the CEO's key quote in a stylized pull-quote box."
```

### 2. Character Consistency & Identity Locking
Supports **up to 14 reference images** (6 with high fidelity).

**Best Practices:**
- **Identity Locking**: "Keep the person's facial features exactly the same as Image 1"
- **Expression/Action**: Describe the *change* in emotion/pose while maintaining identity
- **Viral Composition**: Combine subjects with bold graphics and text in a single pass

**Example:**
```bash
python generate.py "Design a viral video thumbnail using the person from Image 1.
Face Consistency: Keep facial features exactly the same.
Action: Pose them on the left, pointing right with excited expression.
Subject: On the right, a high-quality image of avocado toast.
Graphics: Bold yellow arrow connecting finger to toast.
Text: Overlay '3 Minutes!' in massive pop-style text.
Background: Blurred bright kitchen. High saturation." -i person.jpg
```

### 3. Google Search Grounding
Use `--search` for real-time data, current events, or factual verification.

**Example:**
```bash
python generate.py "Generate an infographic of the best times to visit U.S. National Parks in 2025 based on current travel trends." --search
```

### 4. Advanced Editing & Restoration
The model excels at complex edits via conversational prompting.

**Capabilities:**
- **In-painting**: Remove/add objects naturally
- **Restoration**: Fix old photos
- **Colorization**: Manga/B&W photos
- **Style Swapping**: Transfer styles between images
- **Localization**: Translate text AND adapt to cultural context

**Best Practices:**
- **Semantic Instructions**: No manual masks needed; describe what to change naturally
- **Physics Understanding**: Can handle "fill this glass with liquid"

**Examples:**
```bash
# Remove tourists from photo
python generate.py "Remove the tourists from the background and fill the space with logical textures (cobblestones and storefronts) that match the environment." -i photo.jpg

# Colorize manga
python generate.py "Colorize this manga panel. Use a vibrant anime style palette. Ensure the energy beams are glowing neon blue." -i manga.jpg

# Seasonal change
python generate.py "Turn this scene into winter time. Keep the house exactly the same, but add snow to the roof and yard, and change the lighting to a cold, overcast afternoon." -i house_summer.jpg
```

### 5. Dimensional Translation (2D ↔ 3D)
Translate between 2D schematics and 3D visualizations.

**Example:**
```bash
# Floor plan to 3D interior
python generate.py "Based on this 2D floor plan, generate a professional interior design board. Layout: Large main image (wide-angle of living area), three smaller images below (Master Bedroom, Home Office, 3D top-down floor plan). Style: Modern Minimalist with warm oak wood flooring. Quality: Photorealistic, soft natural lighting." -i floorplan.png
```

### 6. High-Resolution & Textures
Use 4K for detailed textures and large-format prints.

**Best Practices:**
- Explicitly request high resolutions
- Describe high-fidelity details (imperfections, surface textures)

**Example:**
```bash
python generate.py "Harness native high-fidelity output to craft a breathtaking, atmospheric environment of a mossy forest floor. Command complex lighting effects and delicate textures, ensuring every strand of moss and beam of light is rendered in pixel-perfect resolution suitable for a 4K wallpaper." -r 4K
```

### 7. Thinking & Reasoning
Pro model generates interim "thought images" (not charged) to refine composition.

**Capabilities:**
- Solve equations visually
- Analyze images and generate "before" versions
- Visual reasoning and data analysis

### 8. One-Shot Storyboarding
Generate sequential art or storyboards in a single session.

**Example:**
```bash
python generate.py "Create an addictively intriguing 9-part story with 9 images featuring a woman and man in a luxury luggage commercial. The story should have emotional highs and lows, ending on an elegant shot with the logo. The identity of the woman and man and their attire must stay consistent throughout but they can be seen from different angles and distances. Generate images one at a time in 16:9 landscape format."
```

### 9. Structural Control & Layout Guidance
Use input images to control composition and layout.

**Best Practices:**
- **Drafts & Sketches**: Upload hand-drawn sketch to define placement
- **Wireframes**: Use screenshots/wireframes for high-fidelity UI mockups
- **Grids**: Use grid images for tile-based games or LED displays

**Example:**
```bash
# Sketch to polished ad
python generate.py "Create an ad for a gaming product following this sketch layout." -i rough_sketch.jpg

# Wireframe to UI
python generate.py "Create a mock-up for a plush toy rental app following these guidelines." -i wireframe.png
```

---

## Prompt Templates

### Photorealistic Scene
```
A photorealistic [shot type] of [subject], [action or expression], set in [environment].
The scene is illuminated by [lighting description], creating a [mood] atmosphere.
Captured with [camera/lens details], emphasizing [key textures and details].
```

### Infographic
```
Create a [style: clean/retro/technical] infographic about [topic].
Include distinct sections for [section 1], [section 2], and [section 3].
Ensure all text is legible and stylized to match [aesthetic period/style].
```

### Character with Identity Lock
```
[Action description] using the person from Image 1.
Face Consistency: Keep the person's facial features exactly the same as Image 1.
Expression: [describe emotion/expression change]
Action: [describe pose/action]
Background: [describe background]
```

### Product Shot
```
A high-resolution, studio-lit product photograph of [product description]
on [background surface]. The lighting is [setup] to [purpose].
Camera angle: [angle] to showcase [feature]. Sharp focus on [detail].
```

---

## Requirements

- Google API key in environment (`GOOGLE_API_KEY`) - auto-detected
- Python packages: `google-genai`, `Pillow`

```bash
pip install google-genai Pillow
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No image generated" | Prompt may violate content policy, try rephrasing |
| Invalid resolution | Use uppercase: `1K`, `2K`, `4K` |
| Generic/poor results | Use full sentences, not keyword tags |
| Character inconsistency | Add "Keep facial features exactly the same as Image 1" |
| Wrong composition | Upload a rough sketch as input to guide layout |
