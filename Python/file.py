
# 
# Author : Marc Meinhardt
# Build Date : 07/20/2021
# Title : Generative Art
#

from PIL import ImageTk, Image, ImageChops, ImageFilter
import os, os.path


# MARKUP - : Properties

imageName = "chunk1"
fileExtension = ".jpg"

mainDirPath = "."
inputPath = "input"

size_1020 = (1020,1020)

filters = {
    "blur": ImageFilter.BLUR,
    "contour": ImageFilter.CONTOUR,
    "detail": ImageFilter.DETAIL,
    "edge enhance": ImageFilter.EDGE_ENHANCE,
    "edge enhance more": ImageFilter.EDGE_ENHANCE_MORE,
    "emboss": ImageFilter.EMBOSS,
    "find edges": ImageFilter.FIND_EDGES,
    "sharpen": ImageFilter.SHARPEN,
    "smooth": ImageFilter.SMOOTH,
    "smooth more": ImageFilter.SMOOTH_MORE,
    "box blur": ImageFilter.BoxBlur(10),
    "gaussian blur": ImageFilter.GaussianBlur(25),
    "unsharp mark": ImageFilter.UnsharpMask,
}



# MARKUP - : Functions

if __name__ == "__main__":

    for f in os.listdir(inputPath):
        if f.endswith(fileExtension):

            im = Image.open(os.path.join(inputPath,f))   

            fn, fext = os.path.splitext(f)
            print( f, "|", "image size :", im.size, "|", "colour mode: ", im.mode )

            ####################### 

            # MARKUP - : Image Processing
            
            imProcessed = im.filter(ImageFilter.RankFilter(size=3, rank=0))
            imProcessedBlur = im.filter(ImageFilter.BLUR)
            imProcessedEmboss = im.filter(ImageFilter.EMBOSS)
            imProcessedFindEdges = im.filter(ImageFilter.FIND_EDGES)

            ####################### 

            # MARKUP - : save images in folders
            imProcessed.save('./cache/{}{}'.format(fn, fext))


            # MARKUP - : convert to png and save in png folder
            # i.save('./output/pngs/{}.png'.format(fn))

            # MARKUP - : resize and save in 1020 folder
            #i.thumbnail(size_1020)
            #i.save('output/{}_1020{}'.format(fn, fext))













