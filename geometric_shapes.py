# Setup 
import math, turtle 

'''
Regular Polygon
'''

def polygon(shanjay):
    # Setup
    shanjay.color("royalblue")
    shanjay.penup()
    shanjay.goto(-50, 100)
    shanjay.pendown()
    
    sides = int(input("Please enter the number of sides of the polygon: "))
    while sides < 3:
        print("A polygon must have at least 3 sides.")
        sides = int(input("Please enter the number of sides of the polygon: "))
        
    angle = (sides - 2) * 180 // sides
    
    for i in range(sides):
        shanjay.forward(120)
        shanjay.right(180 - angle)
        
    return


'''
Rhombus
'''
def rhombus(shanjay):
    # Setup
    shanjay.color("royalblue")
    shanjay.penup()
    shanjay.goto(-50, 100)
    shanjay.pendown()
    
    angle = int(input("Please enter the angle of the rhombus: "))
    while angle > 180 or angle < 0:
        print("The angle of a rhombus must be between 0 and 180 degrees.")
        angle = int(input("Please enter the angle of the rhombus: "))
    
    for i in range(2):
        shanjay.forward(200)
        shanjay.right(180 - angle)
        shanjay.forward(200)
        shanjay.right(angle)


'''
Concentric Circles
'''

def concentric_circles(shanjay):
    shanjay.color("royalblue")
    shanjay.penup()
    shanjay.goto(-50, 100)
    shanjay.pendown()
    # screen.tracer(0)        # removes tracing
    
    for i in range(360):
        shanjay.forward(2)
        shanjay.right(1)
        
    shanjay.penup()
    shanjay.left(90)
    shanjay.forward(50)
    shanjay.right(90)
    shanjay.pendown()
        
    for i in range(360):
        shanjay.forward(3)
        shanjay.right(1)
    # Can also use shanjay.circle() for simplification 
