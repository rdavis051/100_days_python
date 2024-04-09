from turtle import Turtle, Screen

rob = Turtle()
rob.shape("turtle")
rob.color("red", "green")
screen = Screen()
def move_forwards():
    rob.forward(10)

def move_backwards():
    rob.backward(10)

def counter_clockwise():
    new_heading = rob.heading() + 10
    rob.setheading(new_heading)

def closewise():
    new_heading = rob.heading() - 10
    rob.setheading(new_heading)

def clear():
    rob.clear()
    rob.penup()
    rob.home()
    rob.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=closewise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()