#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import zipfile
from PIL import Image
from datetime import datetime


def print_banner():
    banner = """
    ================================================
               StickerPack Maker
               Created By : Python       
    ================================================
    """
    print(banner)


def process_image(input_path, output_path):
    with Image.open(input_path) as img:
        img = img.convert("RGBA")
        img = img.resize((512, 512))
        img.save(output_path, "WEBP")
        print("Processed: {}".format(output_path))


def create_sticker_package(input_folder, output_folder, package_name, author):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    sticker_zip_path = os.path.join(output_folder, "{}.zip".format(package_name))
    with zipfile.ZipFile(sticker_zip_path, "w") as zipf:
        for filename in os.listdir(input_folder):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, "{}.webp".format(os.path.splitext(filename)[0]))
                process_image(input_path, output_path)
                zipf.write(output_path, os.path.basename(output_path))
        
        metadata_path = os.path.join(output_folder, "metadata.txt")
        with open(metadata_path, "w") as meta_file:
            meta_file.write("Sticker Pack: {}\n".format(package_name))
            meta_file.write("Author: {}\n".format(author))
            meta_file.write("Created on: {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        zipf.write(metadata_path, "metadata.txt")
    
    print("\nSticker Package Created: {}".format(sticker_zip_path))


if __name__ == "__main__":
    print_banner()
    input_folder = input("Enter the folder path containing your images: ").strip()
    output_folder = "output_stickers"
    package_name = input("Enter the sticker package name: ").strip()
    author = input("Enter your name as the author: ").strip()
    
    print("\nProcessing your sticker package...\n")
    create_sticker_package(input_folder, output_folder, package_name, author)
    print("\nAll done! Check the output folder for your sticker package.")
