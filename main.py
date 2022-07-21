#Imports
import turtle
import random

from matplotlib.pyplot import draw

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

#User Inputs Data for star
amnt = int(input("How many stars would you like to draw? "))
for i in range(0, amnt):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    ang = int(input("Enter angle: "))
    n = int(input("Enter number of points: "))
    size = int(input("Enter size: "))
    draw_star(x, y, ang, n, size)

screen.exitonclick()