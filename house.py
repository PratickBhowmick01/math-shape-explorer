'''
House with a triangular roof, a rectangular door, and two square windows.
'''

# Setup 
import turtle 
import math

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("House Drawing")

shanjay = turtle.Turtle()
shanjay.speed(10)
shanjay.penup()
shanjay.goto(-200, -200)
shanjay.pendown()

#=======================================

# House Base
for i in range(4):
    shanjay.forward(300)
    shanjay.left(90)
    
# Shift
shanjay.penup()
shanjay.forward(110)
shanjay.pendown()

# Door 
shanjay.left(90)
shanjay.forward(100)
shanjay.right(90)
shanjay.forward(80)
shanjay.right(90)
shanjay.forward(100)

# Shift
shanjay.penup()
shanjay.left(180)
shanjay.forward(250)
shanjay.right(90)
shanjay.pendown()

# Window
for i in range(4):
    shanjay.forward(50)
    shanjay.right(90)
    
# Shift
shanjay.penup()
shanjay.left(180)
shanjay.forward(130)
shanjay.right(180)
shanjay.pendown()

# Window
for i in range(4):
    shanjay.forward(50)
    shanjay.right(90)
    
# Shift
shanjay.penup()
shanjay.left(90)
shanjay.forward(50)
shanjay.left(90)
shanjay.forward(60)
shanjay.pendown()

# Roof
shanjay.right(135)
shanjay.forward(300 // math.sqrt(2))
shanjay.right(90)
shanjay.forward(300 // math.sqrt(2))
    
screen.exitonclick() 