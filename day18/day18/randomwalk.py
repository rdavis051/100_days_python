import random
import turtle
from turtle import Turtle, Screen

directions = [0, 90, 180, 270]

ti = Turtle()
turtle.colormode(255)
ti.shape("turtle")
ti.pensize(15)
ti.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r, g, b)
    return random_color

for _ in range(200):
    ti.color(random_color())
    ti.forward(30)
    ti.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()