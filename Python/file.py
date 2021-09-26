
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

# MARKUP - : filters
# Rank Filter
# Marble Filter
# Diffuse Filter
# Bump Filter
# Noise Filter
# Pointillize Filter
# Smear Filter
# Despeckle Filter
# Oil Filter
# Sharpen Filter
# Edge Filter
# Laplace Filter

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
    "rank filter": ImageFilter.RankFilter(size=3, rank=0),
    "median": ImageFilter.MedianFilter(size=3),
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
            
            imLevel1_ProcessedRank = im.filter(filters["rank filter"])
            imLevel2_ProcessedRank = imLevel1_ProcessedRank.filter(filters["median"])

            #imProcessedRank = im.filter(ImageFilter.RankFilter(size=3, rank=8))
            #imProcessedMedian = imProcessedRank.filter(ImageFilter.MedianFilter(size=3))
            #imProcessedBlur = imProcessedMedian.filter(ImageFilter.BLUR)
            #imProcessedEmboss = imProcessedBlur.filter(ImageFilter.EMBOSS)
            #imProcessedFindEdges = imProcessedBlur.filter(ImageFilter.FIND_EDGES)

            ####################### 

            # MARKUP - : save images in folders
            imLevel2_ProcessedRank.save('./output/{}_processed{}'.format(fn, fext))

            # MARKUP - : convert to png and save in png folder
            # i.save('./output/pngs/{}.png'.format(fn))

            # MARKUP - : resize and save in 1020 folder
            #i.thumbnail(size_1020)
            #i.save('output/{}_1020{}'.format(fn, fext))













