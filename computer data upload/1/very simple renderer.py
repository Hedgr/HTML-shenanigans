import io

import matplotlib.pyplot as plot
import cv2_rgb as cv2
import matplotlib.image as img
import numpy

#import numpy
#import matplotlib.pyplot as plt
#from PIL import Image as im
#import numpy
#import matplotlib.pyplot as plt
#import imageio as imio
#import matplotlib.cm as cm
#import numpy as np


# Python program to convert
# numpy array to image

# import required libraries
#import numpy as np
#from PIL import Image as im


# define a main function
#def main():
    # create a numpy array from scratch
    # using arange function.
    # 1024x720 = 737280 is the amount
    # of pixels.
    # np.uint8 is a data type containing
    # numbers ranging from 0 to 255
    # and no non-negative integers

    #array = for i in range(100):numpy.full((1,1),255)
    #print(type(array))
    # our array will be of width
    # 737280 pixels That means it
    # will be a long dark line
    #print(array.shape)
    #array = np.reshape(array, (1, 1))
    #print(array)
    #print(array.shape)
    #data = im.fromarray(array,"RGBA")
    #data.save('image.png')

file = io.open("test.txt", "w")
plot.axis("off")



#for i in range(len(image)):
#    for j in range(len(image[i])):
#        file.write("("+str(j)+","+str(i)+")"+str(image[i][j])+"\n")

image=[[[255, 255, 255],[255, 255, 255],[255, 255, 255],[255, 255, 255]],
      [[128, 128, 128],[128, 255, 255],[255, 128, 255],[255, 255, 128]],
      [[0,    0,    0],[0,   255, 255],[255, 0,   255],[255, 255, 0  ]]]
image = []
for i in range(4):
    image.append([])
    for j in range(255):

        if i == 0:
            image[i].append([j, j, j])
        elif i==1:
            image[i].append([j, 0, 0])
        elif i==2:
            image[i].append([0, j, 0])
        else:
            image[i].append([0, 0, j])

file.write(str(image))
plot.imshow(image)
image = numpy.array(image)
im2 = cv2.imread("testimg.jpg")
print(im2)
plot.savefig("image.png")
plot.show()