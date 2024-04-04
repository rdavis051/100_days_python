import random
import turtle
from turtle import Turtle, Screen

leo = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r, g, b)
    return color

leo.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        leo.color(random_color())
        leo.circle(100)
        leo.setheading(leo.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()