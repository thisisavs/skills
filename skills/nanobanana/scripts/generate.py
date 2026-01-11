#!/usr/bin/env python3
"""
NanoBanana Pro - Google Gemini Image Generation
Standalone CLI tool for generating images using Google's Gemini image models.

Models:
  - gemini-3-pro-image-preview (Nano Banana Pro): Professional quality, 4K, thinking mode
  - gemini-2.5-flash-image (Nano Banana): Faster, 1024px, high-volume

Usage:
    python generate.py "your prompt here"
    python generate.py "your prompt" --output image.png
    python generate.py "your prompt" --aspect 16:9 --resolution 2K
    python generate.py "your prompt" --input reference.jpg  # Image editing
    python generate.py "your prompt" --model flash  # Use faster model
"""

from google import genai
from google.genai import types
from PIL import Image
import argparse
import datetime
import os
import sys

# Model options
MODELS = {
    "pro": "gemini-3-pro-image-preview",    # Nano Banana Pro - professional, 4K capable
    "flash": "gemini-2.5-flash-image",       # Nano Banana - faster, 1024px
}

# Valid options
VALID_ASPECT_RATIOS = ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]
VALID_RESOLUTIONS = ["1K", "2K", "4K"]  # Must be uppercase! Pro model only

# Defaults
DEFAULT_MODEL = "pro"
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_RESOLUTION = "2K"
DEFAULT_OUTPUT_DIR = "generated_images"


def generate_image(
    prompt: str,
    output_path: str = None,
    aspect_ratio: str = DEFAULT_ASPECT_RATIO,
    resolution: str = DEFAULT_RESOLUTION,
    model: str = DEFAULT_MODEL,
    input_image_path: str = None,
    use_search: bool = False,
) -> dict:
    """
    Generate an image using Google Gemini image models.

    Args:
        prompt: Text description of the image to generate
        output_path: Optional path to save the image (auto-generated if not provided)
        aspect_ratio: Image aspect ratio (default: 16:9)
                     Valid: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
        resolution: Image resolution (default: 2K, Pro model only)
                   Valid: 1K, 2K, 4K (must be uppercase!)
        model: Model to use - "pro" or "flash" (default: pro)
        input_image_path: Optional input image for editing/style transfer
        use_search: Enable Google Search grounding for real-time data

    Returns:
        dict with status, filepath, and metadata
    """
    # Validate aspect ratio
    if aspect_ratio not in VALID_ASPECT_RATIOS:
        return {
            "status": "error",
            "message": f"Invalid aspect ratio '{aspect_ratio}'. Valid options: {VALID_ASPECT_RATIOS}"
        }

    # Validate resolution (Pro model only)
    if resolution not in VALID_RESOLUTIONS:
        return {
            "status": "error",
            "message": f"Invalid resolution '{resolution}'. Valid options: {VALID_RESOLUTIONS} (must be uppercase!)"
        }

    # Validate model
    if model not in MODELS:
        return {
            "status": "error",
            "message": f"Invalid model '{model}'. Valid options: {list(MODELS.keys())}"
        }

    model_id = MODELS[model]

    try:
        # Create client (uses GOOGLE_API_KEY from environment automatically)
        client = genai.Client()

        # Build contents
        contents = []

        # Add input image if provided (for editing/style transfer)
        if input_image_path:
            if not os.path.exists(input_image_path):
                return {
                    "status": "error",
                    "message": f"Input image not found: {input_image_path}"
                }
            input_image = Image.open(input_image_path)
            contents.append(input_image)

        contents.append(prompt)

        # Build config
        config_dict = {
            "response_modalities": ["TEXT", "IMAGE"],
        }

        # Image config
        image_config = {"aspect_ratio": aspect_ratio}

        # Resolution only for Pro model
        if model == "pro":
            image_config["image_size"] = resolution

        config_dict["image_config"] = types.ImageConfig(**image_config)

        # Google Search grounding (Pro model recommended)
        if use_search:
            config_dict["tools"] = [{"google_search": {}}]

        config = types.GenerateContentConfig(**config_dict)

        # Generate image
        response = client.models.generate_content(
            model=model_id,
            contents=contents,
            config=config,
        )

        # Check for valid response
        if not response.candidates:
            return {
                "status": "error",
                "message": "No image generated. The prompt may have been blocked or failed."
            }

        # Extract image and text from response
        result_text = None
        image_saved = False
        filepath = None

        for part in response.parts:
            if part.text is not None:
                result_text = part.text
            elif part.inline_data is not None:
                # Get image
                image_obj = part.as_image()

                # Determine output path
                if output_path:
                    filepath = output_path
                    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)
                else:
                    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
                    # Use timestamp for unique filename
                    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                    # Determine extension from mime type or default to png
                    ext = "png"
                    if hasattr(part.inline_data, 'mime_type') and part.inline_data.mime_type:
                        ext = part.inline_data.mime_type.split("/")[-1]
                    filepath = os.path.join(DEFAULT_OUTPUT_DIR, f"nano_{timestamp}.{ext}")

                # Save image
                image_obj.save(filepath)
                image_saved = True

        if not image_saved:
            return {
                "status": "error",
                "message": "No image found in response. Model may have returned text only.",
                "text": result_text
            }

        # Get absolute path for clarity
        abs_path = os.path.abspath(filepath)

        return {
            "status": "success",
            "message": "Image generated successfully",
            "filepath": abs_path,
            "filename": os.path.basename(filepath),
            "model": model_id,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution if model == "pro" else "1024px",
            "text": result_text,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Generation failed: {str(e)}"
        }


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Google Gemini (NanoBanana)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic generation (Pro model, 16:9, 2K)
    python generate.py "a fluffy owl in a moonlit forest"

    # Custom output path
    python generate.py "cyberpunk city at night" -o cityscape.png

    # Different aspect ratio and resolution
    python generate.py "portrait of a wizard" -a 3:4 -r 4K

    # Use faster Flash model
    python generate.py "quick sketch of a cat" -m flash

    # Edit an existing image
    python generate.py "add a wizard hat to this cat" -i cat.jpg

    # Use Google Search for real-time data
    python generate.py "weather forecast chart for NYC" --search

Valid aspect ratios: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
Valid resolutions (Pro only): 1K, 2K, 4K (must be uppercase!)

Models:
    pro   - gemini-3-pro-image-preview (default, professional quality, 4K)
    flash - gemini-2.5-flash-image (faster, 1024px max)
        """
    )

    parser.add_argument("prompt", help="Text description of the image to generate")
    parser.add_argument("-o", "--output", help="Output file path (auto-generated if not specified)")
    parser.add_argument("-a", "--aspect", default=DEFAULT_ASPECT_RATIO,
                       help=f"Aspect ratio (default: {DEFAULT_ASPECT_RATIO})")
    parser.add_argument("-r", "--resolution", default=DEFAULT_RESOLUTION,
                       help=f"Resolution: 1K, 2K, or 4K - Pro model only (default: {DEFAULT_RESOLUTION})")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL, choices=["pro", "flash"],
                       help=f"Model: pro or flash (default: {DEFAULT_MODEL})")
    parser.add_argument("-i", "--input", dest="input_image",
                       help="Input image path for editing/style transfer")
    parser.add_argument("--search", action="store_true",
                       help="Enable Google Search grounding for real-time data")

    args = parser.parse_args()

    print(f"Generating image...")
    print(f"  Model: {MODELS[args.model]}")
    print(f"  Prompt: {args.prompt[:80]}{'...' if len(args.prompt) > 80 else ''}")
    print(f"  Aspect: {args.aspect}")
    if args.model == "pro":
        print(f"  Resolution: {args.resolution}")
    if args.input_image:
        print(f"  Input image: {args.input_image}")
    if args.search:
        print(f"  Google Search: enabled")

    result = generate_image(
        prompt=args.prompt,
        output_path=args.output,
        aspect_ratio=args.aspect,
        resolution=args.resolution,
        model=args.model,
        input_image_path=args.input_image,
        use_search=args.search,
    )

    if result["status"] == "success":
        print(f"\nSuccess! Image saved to: {result['filepath']}")
        if result.get("text"):
            print(f"Model response: {result['text']}")
    else:
        print(f"\nError: {result['message']}", file=sys.stderr)
        sys.exit(1)

    return result


if __name__ == "__main__":
    main()
