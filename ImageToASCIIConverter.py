import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# ASCII characters sorted by brightness level
ASCII_CHARS = "@#%WM8&B*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\^`'. "
BACKGROUND_CHAR = " "  # Default background character


def image_to_ascii(
    image_path,
    width=100,
    scale_factor=0.55,
    contrast=1.5,
    sharpen=True,
    background=True,
):
    """
    Converts an image to ASCII format.

    Parameters:
        image_path (str): Path to the input image file.
        width (int): Desired output width in characters.
        scale_factor (float): Factor to adjust the height-to-width ratio.
        contrast (float): Contrast enhancement factor.
        sharpen (bool): Whether to apply sharpening filter.
        background (bool): Whether to include background characters.

    Returns:
        str: ASCII representation of the image.
    """
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert("L")

    # Enhance contrast
    img = ImageEnhance.Contrast(img).enhance(contrast)

    # Apply sharpening filter (optional)
    if sharpen:
        img = img.filter(ImageFilter.SHARPEN)

    # Compute new height while maintaining aspect ratio
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio * scale_factor)
    img = img.resize((width, new_height))

    # Convert pixel values to ASCII characters
    pixels = np.array(img)
    ascii_chars = (
        ASCII_CHARS if background else ASCII_CHARS.replace(BACKGROUND_CHAR, "")
    )
    scale = 255 / (len(ascii_chars) - 1)
    ascii_str = "".join(
        ascii_chars[min(int(pixel / scale), len(ascii_chars) - 1)]
        for row in pixels
        for pixel in row
    )

    # Format into lines
    ascii_str = "\n".join(
        ascii_str[i : i + width] for i in range(0, len(ascii_str), width)
    )

    return ascii_str


# Example usage
if __name__ == "__main__":
    image_path = "./GitHub_Logo.png"  # Path to the input image
    ascii_art = image_to_ascii(
        image_path, width=100, contrast=1.8, sharpen=True, background=False
    )

    # Print ASCII output
    print(ascii_art)

    # Save output to a file
    output_path = "./output.txt"
    with open(output_path, "w") as f:
        f.write(ascii_art)

    print(f"ASCII output saved to: {output_path}")
