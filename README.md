# Image to ASCII Converter

## Description
This project converts an image into an ASCII representation using Python. It processes an input image, enhances its contrast, optionally sharpens it, and maps pixel intensity to ASCII characters to generate a text-based representation of the image.

## Features
- Converts any image into ASCII art
- Adjustable output width
- Configurable contrast enhancement
- Optional sharpening filter for better clarity
- Background customization option (can be enabled or disabled)
- Saves ASCII output to a text file

## Installation

Ensure you have Python installed on your system. Then, install the required dependencies using pip:

```sh
pip install numpy pillow
```

## Usage

1. Place your image file in the project directory.
2. Run the script with the desired parameters:

```sh
python image_to_ascii.py
```

By default, the script uses `./as.png` as the input image. Modify `image_path` in the script to use a different image.

### Parameters
The `image_to_ascii` function accepts the following optional parameters:
- `width` (int): Width of the ASCII output in characters (default: `100`)
- `scale_factor` (float): Adjusts height-to-width ratio (default: `0.55`)
- `contrast` (float): Contrast enhancement factor (default: `1.5`)
- `sharpen` (bool): Apply a sharpening filter (default: `True`)
- `background` (bool): Include background characters in the ASCII output (default: `True`)

Example function call:

```python
ascii_art = image_to_ascii("image.png", width=120, contrast=2.0, sharpen=False, background=False)
```

## Output
The generated ASCII art will be printed to the terminal and saved in `output.txt` in the project directory.

## License
This project is licensed under the MIT License.

## Author
9Obsidyen
