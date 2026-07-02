import os
from PIL import Image

def image_info(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        image_format = img.format
        file_size = os.path.getsize(image_path)

        print("\nImage Information")
        print("-----------------")
        print(f"Dimensions : {width} x {height}")
        print(f"Format     : {image_format}")
        print(f"File Size  : {file_size / 1024:.2f} KB")