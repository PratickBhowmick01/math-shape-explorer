import math, turtle
from geometric_shapes import concentric_circles, rhombus, polygon
from house import house
from traffic_lights import traffic_lights


def main():
    # Setup 
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Math & Shape Explorer")    
    shanjay = turtle.Turtle()
    shanjay.speed(10)
    
    
    while True:
        # Clearing previous drawings
        shanjay.clear()
        shanjay.penup()
        shanjay.home()
        shanjay.pendown()
        
        keyword = input("Enter a keyword: ('house', 'circle', 'polygon', 'rhombus', 'traffic'): ").lower()
        
        if keyword == 'house': house(shanjay)
        elif keyword == 'circle': 
            screen.tracer(0)
            concentric_circles(shanjay)
        elif keyword == 'polygon': polygon(shanjay)
        elif keyword == 'rhombus': rhombus(shanjay)
        elif keyword == 'traffic': traffic_lights(shanjay)
        else: 
            print("Not a valid function.")
            break 
        
        screen.update()
        
        check = input("Do you wish to try another function? Enter Y or N: ").lower()
        if check == "y": 
            continue 
        else: break
        
    turtle.bye()
    
if __name__ == "__main__":
    main()