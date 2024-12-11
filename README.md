# StickerPack Maker 

![Sticker-Maker Jenderal92](https://github.com/user-attachments/assets/cca026ff-01b0-47be-966e-5e49841874bf)


**StickerPack Maker** is a Python-powered tool that allows users to easily create sticker packs for Telegram and WhatsApp. This tool simplifies the process by automating image processing, resizing, and embedding metadata such as the package name and creator's name. The tool also packages the stickers into a ZIP file, ready for upload.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

---

## Features

1. **Automatic Sticker Pack Creation**  
   Simply provide a folder of images, and the tool will handle the conversion, cropping, and resizing to meet Telegram/WhatsApp sticker requirements.

2. **Metadata Embedding**  
   Add package name, description, and creator's name to personalize your sticker pack.

3. **Automatic Format Conversion**  
   Supports conversion from popular image formats (JPG, PNG) to WebP, the standard for Telegram and WhatsApp stickers.

4. **ZIP Packaging**  
   Automatically compresses all processed stickers and metadata into a ZIP file, ready for upload to platforms.


## Requirements

- **Python Version**: Python 2.7 or higher (tested on Python 3.9)
- **Libraries**:
  - [Pillow](https://pypi.org/project/Pillow/)
  - [pywebp](https://pypi.org/project/pywebp/)


## Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/Jenderal92/Sticker-Maker.git
   cd Sticker-Maker
   ```

2. Install the required dependencies:
   ```bash
   pip install pillow pywebp
   ```


## Usage

1. Prepare a folder containing the images you want to use as stickers.
2. Run the script using the following command:
   ```bash
   python sticker_maker.py
   ```
3. Follow the prompts in the terminal:
   - Enter the folder path containing your images.
   - Specify a name for your sticker package.
   - Provide your name as the author.
4. Once the process is complete, a ZIP file containing your stickers and metadata will be available in the output directory.
