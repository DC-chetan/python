from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=400, height=400)
xv=0
for i in range(10):
    tim = Turtle()
    tim.penup()
    tim.shape("square")
    tim.color("white")
    xv-=20
    tim.setposition(xv,0)



screen.exitonclick()