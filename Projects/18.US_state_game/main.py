import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get mouse coordinate
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("./50_states.csv")
all_state = data["state"].to_list()
guessed_states = []
while len(guessed_states)<50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correted", prompt = "Whats state name: ").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guessed_states ]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_missed.csv")
        print(missing_state)
        break

    if answer_state in all_state:
        guessed_states.append(answer_state) 
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # t.write(state_data.state.item())

