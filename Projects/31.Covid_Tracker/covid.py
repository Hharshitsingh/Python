import tkinter as tk
from tkinter import messagebox

FONT = ("Times New Roman", 15, "bold")
CANVAS_FONT = "Times 12 italic"
CANVAS_TITTLE_FONT = "Arial 14 bold"
WINDOW_BACKGROUND = "#f9e5d8"
CANVAS_BACKGROUND = "#fcd5ce"

class CovidTracker():
    def __init__(self, country, state_data, district_data):
        self.country = country
        self.state_api_data = state_data
        self.district_api_data = district_data
        #create window
        self.window = tk.Tk()
        self.window.title("COVID-19 TRACKER")
        self.window.config(padx=30, pady=30, bg=WINDOW_BACKGROUND)
        #0 row elements
        self.state_label = tk.Label(self.window, text="Select State: ", font=FONT, bg=WINDOW_BACKGROUND)
        self.state_label.grid(column=0, row=0, padx=10, pady=10)
        self.state_variable = tk.StringVar(self.window)
        self.state_list = list(self.district_api_data.keys())
        self.state_variable.set(self.state_list[0])
        self.select_state = tk.OptionMenu(self.window, self.state_variable, *self.state_list)
        self.select_state.grid(column=1, row=0, padx=10, pady=10)
        self.select_state_button = tk.Button(self.window, text="Enter", command=self.selected_state)
        self.select_state_button.grid(column=2, row=0, padx=10, pady=10)
        # 1st row elements
        self.district_label = tk.Label(self.window, text="Select District: ", font=FONT, bg=WINDOW_BACKGROUND)
        self.district_label.grid(column=0, row=1, padx=10, pady=10)
        self.district_variable = tk.StringVar(self.window)
        self.district_list = []
        self.district_variable.set("Select District")
        self.select_district = tk.OptionMenu(self.window, self.district_variable, self.district_list)
        self.select_district.grid(column=1, row=1)
        self.select_district_button = tk.Button(self.window, text="Enter", command=self.selected_district)
        self.select_district_button.grid(column=2, row=1, padx=10, pady=10)
        # 2nd row elements
        self.country_canvas = tk.Canvas(width=200, height=200, bg=CANVAS_BACKGROUND, highlightthickness=0)
        self.country_canvas.grid(column=1, row=3, padx=60, pady=10)
        self.state_canvas = tk.Canvas(width=500, height=200, bg=CANVAS_BACKGROUND, highlightthickness=0)
        self.state_canvas.grid(column=0, row=3, padx=20, pady=10 )
        self.district_canvas = tk.Canvas(width=500, height=200, bg=CANVAS_BACKGROUND, highlightthickness=0)
        self.district_canvas.grid(column=2, row=3, padx=20, pady=10 )
        self.print_country_data()
        print(self.district_variable.get())
        self.window.mainloop()

    def print_country_data(self):
        ''' method print country covid result '''
        self.country_active = self.state_api_data[0]["active"]
        self.country_confirmed = self.state_api_data[0]["confirmed"]
        self.country_recovered = self.state_api_data[0]["recovered"]
        self.country_death = self.state_api_data[0]["deaths"]
        self.country_canvas.create_text(100, 20, text = self.country, font= CANVAS_TITTLE_FONT, anchor="center")
        self.country_canvas.create_text(100, 60, text = f"Active : {self.country_active}", anchor="center", font=CANVAS_FONT)
        self.country_canvas.create_text(100, 90, text = f"Confirmed : {self.country_confirmed}", anchor="center", font=CANVAS_FONT)
        self.country_canvas.create_text(100, 120, text = f"Recovered : {self.country_recovered}", anchor="center", font=CANVAS_FONT)
        self.country_canvas.create_text(100, 150, text = f"Death : {self.country_active}", anchor="center", font=CANVAS_FONT)

    def selected_state(self):
        ''' method to get selected state from dropdown menu '''
        self.option_state = self.state_variable.get()
        self.alldistrict_data = self.district_api_data[self.option_state]["districtData"]
        self.district_list = list(self.alldistrict_data.keys())
        self.district_variable.set(self.district_list[0])
        self.select_district = tk.OptionMenu(self.window, self.district_variable, *self.district_list)
        self.select_district.grid(column=1, row=1, padx=10, pady=10)
        self.print_state_data()


    def print_state_data(self):
        ''' method print state covid result '''
        self.state_canvas.delete("all")
        self.state_data = ""
        self.state = self.state_variable.get()
        for states in self.state_api_data:
            if self.state in states["state"]:
                self.state_data = states
        self.state_confired = self.state_data["confirmed"]
        self.state_active = self.state_data["active"]
        self.state_death = self.state_data["deaths"]
        self.state_recoverd = self.state_data["recovered"]
        self.state_canvas.create_text(250, 20, text = f"{self.state}", width = 450 ,font= CANVAS_TITTLE_FONT, anchor="center")
        self.state_canvas.create_text(250, 60, text = f"Active : {self.state_active}", anchor="center", font=CANVAS_FONT)
        self.state_canvas.create_text(250, 90, text = f"Confirmed : {self.state_confired}", anchor="center", font=CANVAS_FONT)
        self.state_canvas.create_text(250, 120, text = f"Recovered : {self.state_recoverd}", anchor="center", font=CANVAS_FONT)
        self.state_canvas.create_text(250, 150, text = f"Death : {self.state_death}", anchor="center", font=CANVAS_FONT)
        self.print_district_data()

    def selected_district(self):
        ''' method to get selected district from dropdown menu '''
        try:
            self.option_district = self.district_variable.get()
            self.district_data = self.alldistrict_data[self.option_district]
            self.print_district_data()
        except AttributeError:
            messagebox.showwarning(title="Warning", message="Select State")

    def print_district_data(self):
        ''' method print district covid result '''
        self.district_canvas.delete("all")
        self.district = self.district_variable.get()
        self.district_data = self.alldistrict_data[self.district]
        self.district_active = self.district_data["active"]
        self.district_confirmed = self.district_data["confirmed"]
        self.district_recoved = self.district_data["recovered"]
        self.district_death = self.district_data["deceased"]
        self.district_canvas.create_text(250, 20, text = f"{self.district}",width = 450, font= CANVAS_TITTLE_FONT, anchor = "center")
        self.district_canvas.create_text(250, 60, text = f"Active : {self.district_active}", anchor="center", font=CANVAS_FONT)
        self.district_canvas.create_text(250, 90, text = f"Confirmed : {self.district_confirmed}", anchor="center", font=CANVAS_FONT)
        self.district_canvas.create_text(250, 120, text = f"Recovered : {self.district_recoved}", anchor="center", font=CANVAS_FONT)
        self.district_canvas.create_text(250, 150, text = f"Death : {self.district_death}", anchor="center", font=CANVAS_FONT)

