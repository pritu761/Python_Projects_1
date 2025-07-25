from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    tim.left(90)
def turn_right():
    tim.right(90)
def clear_screen():
    screen.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=turn_right)
screen.onkey(key="d", fun=clear_screen)
screen.exitonclick()
