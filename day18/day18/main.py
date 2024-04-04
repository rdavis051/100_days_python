from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red", "green")

for x in range(0,4):
    tim.forward(100)
    tim.right(90)

ty = Turtle()
ty.shape("triangle")
ty.color("blue")
ty.setpos(-100,-100)
for _ in range(15):
    ty.forward(10)
    ty.penup()
    ty.forward(10)
    ty.pendown()


screen = Screen()
screen.exitonclick()
