import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0

wordturtle = turtle.Turtle()
wordturtle.penup()
wordturtle.color("black")
wordturtle.hideturtle()

data = pandas.read_csv("50_states.csv")
statelist = data.state.tolist()

correct_states = []


game_on = True

while len(correct_states) < 50:
    answer_state = screen.textinput(title= f"{score}/50 States Correct", prompt="What's another state's name?").title()



    if answer_state == "Exit":
        missing_states = [state for state in statelist if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in statelist:
        stateInfo = data[data.state == answer_state]
        state_x = int(stateInfo.x)
        state_y = int(stateInfo.y)
        wordturtle.goto(x=state_x, y=state_y)
        wordturtle.write(answer_state)
        correct_states.append(answer_state)
        score += 1


# states_to_learn.csv

