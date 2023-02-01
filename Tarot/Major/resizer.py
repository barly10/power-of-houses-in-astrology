from PIL import Image
import PIL
import os
import glob


path = r'*.jpg'
local_files = glob.glob(path)
base_width = 300

for file in local_files:
    image = Image.open(file)
    width_percent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
    image.save(file)

