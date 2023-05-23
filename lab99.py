from PIL import Image, ImageFilter
from pathlib import Path
import os
import shutil


filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

Path('opa').mkdir(parents=True, exist_ok=True)
for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.CONTOUR)
        new_img.save("new_" + file)

files = ["new_1.jpg", "new_2.jpg", "new_3.jpg", "new_4.jpg", "new_5.jpg"]
for file in files:
    path = shutil.move(file, 'opa')


if file.suffix in ['.jpg', '.png']:






