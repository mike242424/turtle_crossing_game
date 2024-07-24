from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f'Level {self.level}', move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.show_score()
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', move=True, align=ALIGN, font=FONT)

