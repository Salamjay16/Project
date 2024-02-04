'''import time
from random import randint

for i in range(1,85):
    print('')

space = ''

for i in range(1,1000):
    count = randint(1, 100)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + '🎂Happy Birthday HAMSEM!')
    elif(i%9 == 0):
        print(space + "🎂")
    elif(i%5==0):
        print(space +"💛")
    elif(i%8==0):
        print(space + "🎉")
    elif(i%7==0):
        print(space + "🍫")
    elif(i%6==0):
        print(space + "Happy Birthday HAMSEM\n AGE WITH GRACE!💖")
    else:
        print(space + "🔸")

    space = ''
    time.sleep(0.1)'''
    
    
'''import _tkinter
import time
import tkinter.font
import turtle
pen = turtle.Turtle()

def curve():
    for i in range(1,200):
        pen.right(1)
        pen.forward(1)
        
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    
def txt():
    pen.up()
    pen.setpos(-75, 75)
    pen.down()
    pen.color('white')
    pen.write("Happy Birtday\n   hamsem", font = ("Times New Roman", 18, "bold", "italic",))
    time.sleep(3)
heart()
txt()
pen.ht()'''


'''import turtle
import random
import time

# sets background
time.sleep(1)
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("red")
turtle.pendown()
turtle.forward(345)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("yellow")
turtle.pendown()
turtle.forward(315)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("blue")
turtle.pendown()
turtle.forward(285)

# Cake
turtle.penup()
turtle.goto(-75,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-65,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-35,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-5,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(25,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(55,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-20,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(15)
    turtle.right(angle)
    turtle.forward(10)

# Happy Birthday message
turtle.penup()
turtle.goto(-100, 50)
turtle.color("blue")
turtle.pendown()
turtle.write("Happy Birthday\n     MOMMY OWOLABI", font = ("Veranda", 20, "bold", "italic",))
turtle.color("red")
time.sleep(3)


 #Area of a trapezoid
                #example_1
import functools
from unittest import result
def Area_of_a_Trapezoid(base_1,base_2,height):
    #Calculate it's Area
    Area_of_a_Trapezoid = 0.5 * (base_1 + base_2) * height
    print("Area of a Trapezoid:",Area_of_a_Trapezoid)
    return result
Area_of_a_Trapezoid(9,6,4)

                #example_2
import math
base_1 = 5
basse_2 = 6
height = float(input("Height of trapezoid in cm:"))
base_1 = float(input('Base 1 value in cm:'))
base_2 = float(input('Base 2 value in cm:'))
area = ((base_1 + base_2) /2 * height)
print("Area is in cm**:", area)'''

'''lst = [0]
for i in range(2, -1, -1):
    for j in range(6,9,2):
        lst.append(i+j)
    
print(lst)''' 

'''import matplotlib.pyplot as plt
x = [24,25,26]
y = [23,24,25]
plt.plot(x,y)
plt.show()'''
                     

"""import sys
import webbrowser
from datetime import datetime

def main():
    while True:
        now = datetime.now().strftime("%I:%M %p") 
        if now == "05:15 PM":
            # webbrowser.open("https://fsbn.com.ng/applicants/scholarships/printout/28527")  
            sys.exit(0)
            
if __name__ == "__main__":
    main()             """         
    
    
'''[1,2] + [3,4]'''
'''class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year
    
    def __str__(self):
        return f"FunEvent(tags=[self.tags], year=[self.year])"
    
tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags, year)
tags.append("bootcamp") 
year = 2023
print(bootcamp)'''   

"""def tail(filename, n=10):
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines[-n:]:
        print(line)"""          
        

'''Content of "log.txt":
10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 2222
10.1.1.9 - bike [01/Mar/2022:13:05:10 +0900] "GET /python HTTP/1.0" 200 2222

Expected output:
01/Mar/2022:13:05:05 +0900
01/Mar/2022:13:05:10 +0900

from asyncio import log


log.txt = [0 1/Mar/2022:13:05:05 +0900] 

import re
def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])

def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))

def parse3():
    for line in open("log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))
        
def parse4():
    for line in open("log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))
  
def parse5():
    for line in open("log.txt"):
        print(re.split("\[|\]", line)[1]) '''                      
        

'''def sqsum4(nums):
   return sum(x**2 for x in nums if x > 0)
   
def sqsum2(nums):
   return sum(x^2 for x in nums if x > 0)

def sqsum1(nums):
    return sum(x**2 if x > 0 for x in nums)

def sqsum3(nums):
   return sum(for x in nums if x > 0 then x^2)

def sqsum5(nums):
   return sum(x^2 if x > 0 for x in nums)'''  

    
                                                
                                                

# class FunEvent:
#     def __init__(self, tags, year):
#        self.tags = tags
#        self.year = year
    
#     def __str__(self):
#         return f"FunEvent(tags={self.tags}, year={self.year})"

# tags = ["google", "ml"]
# year = 2022
# bootcamp = FunEvent(tags, year)
# tags.append("bootcamp")
# year = 2023
# print(bootcamp)      

# x = int(input("what's the value of a? "))
# y = int(input("what's the value of b? "))
# c = x + y
# print(c) 
           


import base64
from imp import reload
import unicodedata   
### Part 1
### Reversing the message
'''print("--- Part 1 ---")

backwards_message = "edoc ot nrael ot tnaw I"
print("The backwards message is:", backwards_message)
# TODO: Copy and paste the code to flip the message here
print("--- Part 1 ---")
backwards_message = "edoc ot nrael ot tnaw I"
print("The backwards message is:", backwards_message[::-1])'''

### Part 2
### Base64 decoding
print("\n--- Part 2 ---")
encoded_message = "SSB3YW50IHRvIHdvcmsgdG9nZXRoZXI="
print("The encoded message is", encoded_message)

# TODO: Copy and paste the code to decode the message here

print("\n--- Part 2 ---")
decoded_message = base64.b64decode(encoded_message.encode('ascii')).decode('ascii')
print("The encoded message is:", decoded_message)

### Part 3
### Decrypting with a key
print("\n--- Part 3 ---")

encrypted = "N%|fsy%yt%rfpj%sj|%kwnjsix"
print("The encrypted message is:", encrypted)

# TODO: Find the key that correctly decrypts the message
key = 5

print("Trying key:", key)

decrypted = ""
for letter in encrypted:
  decrypted += chr(ord(letter) - key)
print("The decrypted message is:", decrypted) 

## Part 4
### Putting it all together
print("\n--- Part 4 ---")

full_secret_message = 'N\\>nfZxl^r6ugLRlg8VliL:mi~GONH:\x7f_L:qf]OrNMiqgnGqf7KyNL>5NMWz^]hlXXFzhr[tiL[sg8Vlf8O{i~G{iHG5grK8NJplQr[pg7Rlg8VlgsOm_\\|lg8VliL:mi~GO'
print("The full secret message is:", full_secret_message)

# TODO: Decrypt the message with the key
print("\n--- Part 4 ---")
# full_secret_message = 'N\\>nfZxl^r6ugLRlg8VliL:mi~GONH:\x7f_L:qf]OrNMiqgnGqf7KyNL>5NMWz^]hlXXFzhr[tiL[sg8Vlf8O{i~G{iHG5grK8NJplQr[pg7Rlg8VlgsOm_\\|lg8VliL:mi~GO

print("\n--- Decrypt the message with the key ---")
decrypted = ""
for letter in full_secret_message:
  decrypted += chr(ord(letter) - key)

# TODO: Use base64 to decode the message
print("\n--- Using base64 to decode the message ---")
# decoded = decrypted.encode('ascii')
decoded = base64.b64decode(decrypted.encode('ascii')).decode('ascii')

# TODO: Reverse the message
print("\n--- Reversing the message ---")
decrypted_message = decoded[::-1]
print("The decrypted message is:", decrypted_message) 

# https://meet.google.com/jax-ighj-zci
# decoded = decrypted.encode('ascii', 'ignore')
# decoded = base64.b64decode(decrypted) #.encode('ascii')).decode('ascii')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                