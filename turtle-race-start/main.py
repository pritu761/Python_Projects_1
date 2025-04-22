from turtle import Turtle, Screen
import random
colors=['red', 'orange', 'yellow', 'green', 'blue', 'violet']
tim = Turtle()
tim.shape('turtle')
screen = Screen()
screen.setup(500,400)
tim.penup()
tim.goto(-250,-200)
rim = Turtle()
rim.penup()
rim.goto(-250,-180)
kim = Turtle()
kim.penup()
kim.goto(-250,-160)
jim = Turtle()
jim.penup()
jim.goto(-250,-140)
sim = Turtle()
sim.penup()
sim.goto(-250,-120)
rim.shape('turtle')
kim.shape('turtle')
jim.shape('turtle')
sim.shape('turtle')
rim.color(colors[0])
kim.color(colors[1])
jim.color(colors[2])
sim.color(colors[3])
tim.color(colors[4])
all_turtle = [tim, rim, kim, sim, jim]
make_bet = input("Would you like to make a bet?")
is_on = False
if make_bet:
    is_on =  True
while is_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            if make_bet == turtle.color():
                print(f"You have won {turtle}")
            else:
                print(f"You lost {turtle}")
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)
screen.exitonclick()