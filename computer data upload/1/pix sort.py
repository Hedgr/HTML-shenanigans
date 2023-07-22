import io
import matplotlib.pyplot as plot
import cv2_rgb as cv2
import matplotlib.image as img
import numpy

file = io.open("output.txt","w")
plot.axis("off")
plot.rcParams['figure.facecolor'] = 'none'
input_im = img.imread("C:\\Users\\hedgr\\Downloads\\person.png")

mask1 = []
mask2 = []

image = []
# 224x138

def display(img_array, out_file):
    out = io.open(str(out_file),"w")
    for i in range(len(img_array)):
        out.write(str(img_array[i])+"\n")

#make input mask
for i in range(len(input_im)):
    mask1.append([])
    for j in range(len(input_im[i])):
        brightness = round(((input_im[i][j][0]*255)+(input_im[i][j][1]*255)+(input_im[i][j][2]*255))/3,0)
        #print(brightness)
        if (brightness >= 100)&(brightness <= 175):
            mask1[i].append([255,255,255])
        else:
            mask1[i].append([50,50,50])

for i in range(len(input_im)):
    mask2.append([])
    for j in range(len(input_im[i])):
        mask2[i].append([0])
    prev = 0
    count = 0
    startj = 0
    for j in range(len(input_im[i])):
        if mask1[i][j][0] == 255:
            if prev == 0:
                prev = 1
                count = 1
                startj = j
            else:
                count += 1
        else:
            if prev == 1:
                mask2[i][startj][0] = count
            else:
                mask2[i][j][0] = 0
            prev = 0

#c'est la heure de pixel sorting

#for i in range(len(input_im)):
#    current_span = 0
#    for j in range(len(input_im[i])):
#        if mask2[i][j] > 0:
#            current_span = mask2[i][j]




#for i in range(4):
#    image.append([])
#    for j in range(255):
#
#        if i == 0:
#            image[i].append([j, j, j])
#        elif i==1:
#            image[i].append([j, 0, 0])
#        elif i==2:
#            image[i].append([0, j, 0])
#        else:
#            image[i].append([0, 0, j])

display(image, "output.txt")

display(input_im,"very_compressed_mountain.txt")
#file = io.open("output2.txt","w")
#file.write(str(mask1))
display(mask1,"output2.txt")
plot.imshow(mask2)
plot.savefig("image2.png", transparent=True)
display(mask2,"output3.txt")
plot.imshow(mask1)
image = numpy.array(mask1)
plot.savefig("image.png", transparent=True)
plot.show()