from PIL import Image

import os

i = 1

# https://www.pythonpool.com/python-loop-through-files-in-directory/
for filename in os.listdir("orig"):
    f = os.path.join("orig",filename)
    if os.path.isfile(f):

        # https://www.geeksforgeeks.org/python-pil-image-crop-method/
        im = Image.open(f)
        width, height = im.size

        left = 860
        right = 2110
        top = 0
        bottom = height

        im1 = im.crop((left, top, right, bottom))
        name = "babylonian-glossary-" + str(i) + ".png"
        im1 = im1.save(name)

        print("Finished " + str(i))
        i += 1