from turtle import Turtle, Screen
import random

mike = Turtle()

colors = ['red', 'blue', 'green', 'purple', 'black', 'DeepSkyBlue', 'DarkOrchid', 'LightSeaGreen', 'Wheat', 'IndianRed']

def draw_shape(sides):
    rand_int = random.randint(0, len(colors) - 1)
    mike.color(colors[rand_int])
    for x in range(sides):
        mike.forward(100)
        mike.right(360 / sides)

for shape_side_n in range(3,11):
    draw_shape((shape_side_n))


screen = Screen()
screen.exitonclick()