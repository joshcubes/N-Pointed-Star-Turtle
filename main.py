#Imports
import turtle
import random

#variables
scr_x = 800
scr_y = 600

#setup screen
screen = turtle.Screen()
screen.setup(scr_x, scr_y)
screen.bgcolor("white")
screen.title("Stars")

#functions
def draw_odd_star(x, y, size, angle, n):
    turn = 180 - 180 / n
    turtle.seth(angle)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(0, n):
        turtle.forward(size/2)
        turtle.right(turn)
        turtle.forward(size/2)

    turtle.end_fill()

draw_odd_star(0, 0, 100, 0, 5)
screen.exitonclick()