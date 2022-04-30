import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
state_guessed = []

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()


while len(state_guessed) < 50:
    answer_state = screen.textinput(title=f" {len(state_guessed)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Create a popup boxes
    # Upper first Letter
    # Exit game and print all remaining State to csv file when we type "Exit" to popup boxes.
    # While loop can exit out of it as long as we use break statement.

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in state_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in state_guessed:
        state_guessed.append(answer_state)
        state = data[data.state == answer_state]
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.goto(x=int(state.x), y=int(state.y))
        # answer.write(state.state.item())
        answer.write(answer_state)

screen.exitonclick()
