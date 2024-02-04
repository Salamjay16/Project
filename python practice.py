 # Prime Number with given boundaries
# minimum = int(input("Enter the min : "))
# maximum = int(input("Enter the max : "))
# for n in range(minimum,maximum+1):
#     if n > 1:
#         for i in range(2,n):
#             if (n % i) == 0:
#                 break
#         else:
#              print(n)


# Prime numbers with Range
# number = int(input("Enter range:"))
# print("Prime numbers:",end= ' ') 
# for n in range(1,number):
#     for i in range(2,n):
#         if (n % i == 0):
#             break
#     else:
#         print(n, end=' ')


# Sorting elements in the list
# method - 1
# mylist = [5,8,9,6,3]
# for i in range(len(mylist)):
#     #print(mylist[i]) is 5,8,9,6,3
#     for j in range(i+1,len(mylist)):
#         #print(mylist[j]) is 8,9,6,3 9,6,3 6,3 3
#         if mylist[j] < mylist[i]:
#             mylist[i],mylist[j] = mylist[j],mylist[i]
 
# print(mylist)


# def func(x):
#     if x <=1:
#         return 1
#     else:
#         return x * func(x - 1)
    
# print(func(10))


# mm = ({"number" : [5,7,2,4,5],
#        "stage" : ["ss","fv","sd","we","nb"]})
# print(mm)


from PIL import Image, ImageFilter

img = Image.open("C:\Users\USER\Desktop\jay\phone pics\jay.jpeg")
filtered_img = img.filter(ImageFilter.BLUR)
print(img)


# import cv2
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib as plt
# # %matplotlib inline

# def sketch(image):
#     img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
#     canny_edges = cv2.Canny(img_gray_blur, 10, 70)
#     ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
#     return mask
# cap = cv2.VideoCapture(0)
# while True: 
#     ret, frame = cap.read()
#     cv2.imshow('Our Live Sketcher', sketch(frame))
#     if cv2.waitKey(1) == 5:
#         break
# cap.release()
# cv2.destroyAllWindows


       