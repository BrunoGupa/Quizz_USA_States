import turtle
import pandas as pd
from state_name import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

state_name = StateName()

correct_answers = 0
turn_on = True

data = pd.read_csv("50_states.csv")
lower_states = data.state.str.lower()
#print(print(lower_states))


while turn_on:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?")
    column_state = data[data.state.str.lower() == answer_state.lower()]

    if not column_state.empty:
        correct_answers += 1
        state_name.update_state(column_state)

    if correct_answers == 50:
        turn_on = False



screen.exitonclick()


# Get the coordinates with one click
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
