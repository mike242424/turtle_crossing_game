from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(arg=f'Level {self.level}', move=True, align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.update()
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', move=True, align=ALIGN, font=FONT)

