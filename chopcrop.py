#!/usr/bin/python3

from PIL import Image
from rembg import bg
import glob
import sys
import os

# https://github.com/danielgatis/rembg
# https://stackoverflow.com/a/14211878/1248177

if len(sys.argv) < 2:
    print("Usage: rembgs \"*.png\"")
    exit()

path = sys.argv[1]
for filename in glob.glob(path):
    output_path = "rembg_" + filename + ".png"
    with open(filename, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = bg.remove(input)
            o.write(output)

    image = Image.open(output_path)
    imageBox = image.getbbox()
    cropped = image.crop(imageBox)
    cropped.save("cropped_"+output_path)
    os.remove(output_path)


print("done")
