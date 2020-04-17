from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
import numpy
# Performing manimpulation over images...
# 1)creatinig objects of the images and converting them to 'rgba'.
image1=Image.open('gas.jpg').convert('RGBA')
image2=Image.open('gas1.png').convert('RGBA')

# Performing blend operation..
Image.blend(image1,image2,0.3).show()
# Difference between images with and without filter.
ImageChops.difference(image1,image2).show()
# Performing filters...
img=image1.filter(ImageFilter.BoxBlur(9)).show()

