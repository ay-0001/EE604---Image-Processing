# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 00:28:47 2022

@author: AAY
"""
from PIL import Image
import numpy as np
import cv2 as cv
import sys

image = Image.open(sys.argv[1])
#print(image.format)
#print(image.size)
#print(image.mode)

np_image = np.array(image)
np_im1 = np.array(image)
np.set_printoptions(threshold=np.inf)
#print(np_image[0][0])

img_flip_ud = cv.flip(np_image, 0)
#print(np_image[205][0])
for i in range(0,210):
    for j in range(0,190):
        #temp = np_image[i][j]
        np_image[i][j] = np_im1[409-i][j]
for i in range(210,410):
    for j in range(0,190):
        np_image[i][j] = np_im1[i-210][j]
        
np_im2 = np_image

#for i in range(0,210):
#    for j in range(0,190):
#        #temp = np_image[i][j]
 #       np_image[i][j] = np_im2[199-i][j]      
#print(np_image[0][0])
#print(np_image[205][0])
#print(np_image[0])


for i in range(148,324):
    for j in range(516,607):
        np_image[i][j] = np_im1[i][516+(696-j)]

for i in range(148,324):
    for j in range(607,697):
        np_image[i][j] = np_im1[i][606+(607-j)]
        

 
#for i in range(0,210):
 #   for j in range(0,190):
  #      temp = np_image[i][j]
   #     np_image[i][j] = np_image[209-i][j]
    #    np_image[209-i][j] = temp
    

for i in range(369,421):
    for j in range(371,797):
        np_image[i][j] = np_im1[420-(i-369)][j]


for i in range(210,410):
    for j in range(0,190):
        np_image[i-12][j] = np_image[i][j]
        

    
    
    
    
    
img = Image.fromarray(np_image, 'RGB')
img.save('jigsolved.jpg')

#img2 = Image.fromarray(np_im2, 'RGB')
#img2.save('tes.jpg')


flipi = Image.fromarray(img_flip_ud, 'RGB')


#img.save('flipim.jpg')
#cv.imwrite("jigsolved.jpg",np_image)


































