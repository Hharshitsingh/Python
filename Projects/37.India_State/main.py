from datetime import date
from turtle import *
import pandas
class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("India State")
        self.screen.setup(width=600, height=700)
        image = "./india-map.gif"
        self.screen.addshape(image)
        shape(image)
        self.data = pandas.read_csv("./all_state.csv")
        self.all_state = self.data["state"].to_list()
        self.guessed_states = []
        self.take_input()
        self.screen.exitonclick()


    def take_input(self):
        missing_state = []
        while len(self.guessed_states)<36:
            self.answer_state = self.screen.textinput(title= f"{len(self.guessed_states)}/36 States Correted", prompt = "Whats state name: ").title()
            if self.answer_state == "Exit":

                missing_state = [state for state in self.all_state if state not in self.guessed_states ]
                new_data = pandas.DataFrame(missing_state)
                new_data.to_csv("state_missed.csv")
                # print(missing_state)
                for self.answer_state in missing_state:
                    self.add_state()
                break
            self.add_state()
            
    def add_state(self):
            if self.answer_state in self.all_state:
                self.guessed_states.append(self.answer_state) 
                t = Turtle()
                t.hideturtle()
                t.shape('circle')
                t.shapesize(0.5)
                t.penup()
                state_data = self.data[self.data.state == self.answer_state]
                t.goto(int(state_data.cordX), int(state_data.cordY))
                # t.write(self.answer_state)
                t.write(self.answer_state, move=False, align='center', font=('Arial', 8, 'normal'))

start = Game()

