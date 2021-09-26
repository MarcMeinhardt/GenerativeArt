# Import the necessary libraries
from PIL import Image
from numpy import asarray
  
  
# load the image and convert into 
# numpy array
img = Image.open('./input/chunk1.png')
numpydata = asarray(img)
  
# MARKUP - : filter creation 
def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!

    # # this is the non vectorized version
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor

    # faster version that leverages numpy
    new_im.array = image.array * factor

    return new_im


# data
print(numpydata)