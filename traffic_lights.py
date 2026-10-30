# Setup 
import math, turtle 

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Traffic Lights")

shanjay = turtle.Turtle()
shanjay.speed(10)
shanjay.penup()
shanjay.goto(-200, 100)
shanjay.pendown()

#===============================

# Base 
shanjay.fillcolor("black")
shanjay.begin_fill()

for i in range(2):
    shanjay.forward(400)
    shanjay.right(90)
    shanjay.forward(200)
    shanjay.right(90)
    
shanjay.end_fill()
    
    
# Circle1
shanjay.fillcolor("red")
shanjay.begin_fill()

shanjay.penup()
shanjay.goto(-120, -50)
shanjay.pendown()
shanjay.circle(50)

shanjay.end_fill()


# Circle2
shanjay.fillcolor("yellow")
shanjay.begin_fill()

shanjay.penup()
shanjay.goto(0, -50)
shanjay.pendown()
shanjay.circle(50)

shanjay.end_fill()


# Circle3
shanjay.fillcolor("green")
shanjay.begin_fill()

shanjay.penup()
shanjay.goto(120, -50)
shanjay.pendown()
shanjay.circle(50)

shanjay.end_fill()


screen.exitonclick()
