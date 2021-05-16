import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()
states_xcor = states_data.x.tolist()
states_ycor = states_data.y.tolist()

score = 0

correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="                What's another state's name?               ")
    user_input = answer_state.title()

    if user_input == "Exit":
        not_guessed = [state for state in states_list if state not in correct_guesses]
        missing_states_df = pandas.DataFrame(not_guessed)
        missing_states_df.to_csv("missing_states.csv")
        break

    for state in range(0, len(states_list)):
        if user_input == states_list[state]:
            correct_guesses.append(user_input)
            state_name = turtle.Turtle()
            state_name.penup()
            state_name.hideturtle()
            state_name.goto(states_xcor[state], states_ycor[state])
            state_name.write(user_input)
            score += 1
