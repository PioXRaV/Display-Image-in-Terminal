import climage
from PIL import Image

img_d = input("Enter the directory where the image is located.\n---> ")

img = Image.open(img_d)
width = img.width

output = climage.convert(img_d, width=width)

print("\n" + output)