from turtle import Turtle 
from turtle import Screen

turtle = Turtle()
from colorsys import *

turtle.speed(10.5)
turtle.hideturtle()
Colors = ["black", "green", "blue", "red"]

for i in range(150):
    for c in Colors:
        turtle.color(c)
        turtle.left(200)
        turtle.circle(200 - i, 80)
screen = Screen()


screen.exitonclick
