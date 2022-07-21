#Imports
import turtle, random

#variables
scr_x = 800
scr_y = 600
unknown_calc = 0

#setup screen
screen = turtle.Screen()
screen.setup(scr_x, scr_y)
screen.bgcolor("white")
screen.title("Stars")

#setup turtle
turtle.showturtle()
turtle.shape("turtle")

#functions
def intinput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

def intinputrange(prompt, min, max):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number between " + str(min) + " and " + str(max) + ".")

def draw_star(x, y, ang, n, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(ang)
    turtle.pendown()

    extent = 360 / n
    if n % 2 == 0:
        coords = []

        for a in range(0, n):
            turtle.penup()
            coords.append(turtle.pos())
            turtle.circle(size, extent)

        for b in range(0, len(coords)):
            if b % 2 == 0:
                turtle.pendown()
                turtle.goto(coords[b][0], coords[b][1])
            else:
                continue

        turtle.goto(coords[0][0], coords[0][1])
        turtle.penup()

        for c in range(0, (len(coords) + 1)):
            if c % 2 != 0:
                turtle.goto(coords[c][0], coords[c][1])
                turtle.pendown()
            else:
                continue

        turtle.goto(coords[1][0], coords[1][1])

    else:
        angle = 180 - (180 / n)
        for a in range(n):
            turtle.forward(size)
            turtle.right(angle)

def ranstars():
    amnt = intinput("How many stars would you like to draw? ")
    for i in range(0, amnt):
        x = random.randint(scr_x*-1, scr_x)
        y = random.randint(scr_y*-1, scr_y)
        ang = random.randint(0, 360)
        n = random.randint(5, 50)
        size = random.randint(1, 100)
        draw_star(x, y, ang, n, size)

def manstars():
    amnt = int(input("How many stars would you like to draw? "))
    for i in range(0, amnt):
        x = intinput("Enter x coordinate: ")
        y = intinput("Enter y coordinate: ")
        ang = intinput("Enter angle: ")
        n = intinput("Enter number of points: ")
        size = intinput("Enter size: ")
        draw_star(x, y, ang, n, size)

#User Inputs Data for star
speed = intinput("Enter speed: ")
turtle.speed(speed)

choice = intinputrange("Would you like to draw stars manually or randomly? \n1. Random \n2. Manual \n", 1, 2)
if(choice == 1):
    ranstars()
elif(choice == 2):
    manstars()


screen.exitonclick()