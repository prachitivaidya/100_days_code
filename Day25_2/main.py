import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
imag = "blank_states_img.gif"
screen.addshape(imag)
turtle.shape(imag)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50  states Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("50_states_to_learn.csv")
        break
    # if ans state is one of the state from all the states
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #t.write(state_data.state.item())# item fetch first value
        t.write(answer_state)




turtle.mainloop()




