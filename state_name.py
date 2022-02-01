from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_state(self, state_column):
        #self.clear()
        #self.goto(-260, 170)
        self.goto(state_column.x.item(), state_column.y.item())
        self.write(f"{state_column.state.item()}", move=True, align=ALIGNMENT, font=FONT)


