import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv("50_states.csv")
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count = 0
lister = data.state.to_list()
guessed_state = []
left_state=[]
while len(guessed_state) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 are correct", prompt="Which state would you like to guess?").title()
    if answer_state == "Exit":
        for state in lister:
            if state not in guessed_state:
                left_state.append(state)
        break
    if answer_state in lister:
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_row = data[data.state == answer_state]
        tim.goto(state_row.x.item(), state_row.y.item())  #returns only the single name not the the coloumn number
        tim.write(state_row.state.item())
        count += 1
        guessed_state.append(answer_state)
print(left_state)
screen.exitonclick()
