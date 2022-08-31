# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:50:13 2022

@author: AAY
"""

from PIL import Image
import numpy as np
import cv2 as cv
import sys

def f1(x):
    if(x==0):
        cv.circle(img,(50,30),25,(255),-1)
    elif(x==1):
        cv.circle(img,(330,30),25,(255),-1)
    return 1
def f2(x):
    if(x==0):
        cv.circle(img,(110,30),25,(255),-1)
    elif(x==1):
        cv.circle(img,(390,30),25,(255),-1)    
    return 1
def f3(x):
    if(x==0):
        cv.circle(img,(170,30),25,(255),-1)
    elif(x==1):
        cv.circle(img,(450,30),25,(255),-1)    
    return 1
def f4(x):
    if(x==0):
        cv.circle(img,(50,90),25,(255),-1)
    elif(x==1):
        cv.circle(img,(330,90),25,(255),-1)
    return 1
def f5(x):
    if(x==0):
        cv.circle(img,(110,90),25,(255),-1)
    elif(x==1):
        cv.circle(img,(390,90),25,(255),-1)
    return 1
def f6(x):
    if(x==0):
        cv.circle(img,(170,90),25,(255),-1)
    elif(x==1):
        cv.circle(img,(450,90),25,(255),-1)
    return 1
def f7(x):
    if(x==0):
        cv.circle(img,(50,150),25,(255),-1)
    elif(x==1):
        cv.circle(img,(330,150),25,(255),-1)
    return 1
def f8(x):
    if(x==0):
        cv.circle(img,(110,150),25,(255),-1)
    elif(x==1):
        cv.circle(img,(390,150),25,(255),-1)
    return 1
def f9(x):
    if(x==0):
        cv.circle(img,(170,150),25,(255),-1)
    elif(x==1):
        cv.circle(img,(450,150),25,(255),-1)
    return 1
def f10(x):
    if(x==0):
        cv.circle(img,(50,210),25,(255),-1)
    elif(x==1):
        cv.circle(img,(330,210),25,(255),-1)
    return 1
def f11(x):
    if(x==0):
        cv.circle(img,(110,210),25,(255),-1)
    elif(x==1):
        cv.circle(img,(390,210),25,(255),-1)
    return 1
def f12(x):
    if(x==0):
        cv.circle(img,(170,210),25,(255),-1)
    elif(x==1):
        cv.circle(img,(450,210),25,(255),-1)
    return 1
def f13(x):
    if(x==0):
        cv.circle(img,(50,270),25,(255),-1)
    elif(x==1):
        cv.circle(img,(330,270),25,(255),-1)
    return 1
def f14(x):
    if(x==0):
        cv.circle(img,(110,270),25,(255),-1)
    elif(x==1):
        cv.circle(img,(390,270),25,(255),-1)
    return 1
def f15(x):
    if(x==0):
        cv.circle(img,(170,270),25,(255),-1)
    elif(x==1):
        cv.circle(img,(450,270),25,(255),-1)
    return 1

n = int(sys.argv[1])
b = n%10
a = int((n-b)/10)
#print(a,b)
img = np.zeros((300,500,1),dtype= np.uint8)
#im = Image.fromarray(img)
#im.save("black.png")
#cv.circle(img,(50,30),25,(255),-1)
if a == 0:
    f1(0)
    f2(0)
    f3(0)
    f6(0)
    f9(0)
    f12(0)
    f15(0)
    f4(0)
    f7(0)
    f10(0)
    f13(0)
    f14(0)
if a == 1:
    f3(0)
    f6(0)
    f9(0)
    f12(0)
    f15(0)
if a == 2:
    f1(0)
    f2(0)
    f3(0)
    f6(0)
    f7(0)
    f8(0)
    f9(0)
    f10(0)
    f13(0)
    f14(0)
    f15(0)
if a == 3:
    f1(0)
    f2(0)
    f3(0)
    f6(0)
    f7(0)
    f8(0)
    f9(0)
    f12(0)
    f13(0)
    f14(0)
    f15(0) 
if a == 4:
    f1(0)
    f4(0)
    f7(0)
    f8(0)
    f3(0)
    f6(0)
    f9(0)
    f12(0)
    f15(0)   
if a == 5:
    f1(0)
    f2(0)
    f3(0)
    f4(0)
    f7(0)
    f8(0)
    f9(0)
    f12(0)
    f13(0)
    f14(0)
    f15(0)    
if a == 6:
    f1(0)
    f2(0)
    f3(0)
    f4(0)
    f7(0)
    f8(0)
    f9(0)
    f10(0)
    f12(0)
    f13(0)
    f14(0)
    f15(0)       
if a == 7:
    f1(0)
    f2(0)
    f3(0)
    f6(0)
    f9(0)
    f12(0)
    f15(0)
if a == 8:
    f1(0)
    f2(0)
    f3(0)
    f4(0)
    f6(0)
    f7(0)
    f8(0)
    f9(0)
    f10(0)
    f12(0)
    f13(0)
    f14(0)
    f15(0)   
if a == 9:
    f1(0)
    f2(0)
    f3(0)
    f4(0)
    f6(0)
    f7(0)
    f8(0)
    f9(0)
    f12(0)
    f13(0)
    f14(0)
    f15(0)    


if b == 0:
    f1(1)
    f2(1)
    f3(1)
    f6(1)
    f9(1)
    f12(1)
    f15(1)
    f4(1)
    f7(1)
    f10(1)
    f13(1)
    f14(1)
if b == 1:
    f3(1)
    f6(1)
    f9(1)
    f12(1)
    f15(1)
if b == 2:
    f1(1)
    f2(1)
    f3(1)
    f6(1)
    f7(1)
    f8(1)
    f9(1)
    f10(1)
    f13(1)
    f14(1)
    f15(1)
if b == 3:
    f1(1)
    f2(1)
    f3(1)
    f6(1)
    f7(1)
    f8(1)
    f9(1)
    f12(1)
    f13(1)
    f14(1)
    f15(1) 
if b == 4:
    f1(1)
    f4(1)
    f7(1)
    f8(1)
    f3(1)
    f6(1)
    f9(1)
    f12(1)
    f15(1)   
if b == 5:
    f1(1)
    f2(1)
    f3(1)
    f4(1)
    f7(1)
    f8(1)
    f9(1)
    f12(1)
    f13(1)
    f14(1)
    f15(1)    
if b == 6:
    f1(1)
    f2(1)
    f3(1)
    f4(1)
    f7(1)
    f8(1)
    f9(1)
    f10(1)
    f12(1)
    f13(1)
    f14(1)
    f15(1)       
if b == 7:
    f1(1)
    f2(1)
    f3(1)
    f6(1)
    f9(1)
    f12(1)
    f15(1)
if b == 8:
    f1(1)
    f2(1)
    f3(1)
    f4(1)
    f6(1)
    f7(1)
    f8(1)
    f9(1)
    f10(1)
    f12(1)
    f13(1)
    f14(1)
    f15(1)   
if b == 9:
    f1(1)
    f2(1)
    f3(1)
    f4(1)
    f6(1)
    f7(1)
    f8(1)
    f9(1)
    f12(1)
    f13(1)
    f14(1)
    f15(1)  

    
    









cv.imwrite("dotmatrix.jpg",img)#last
