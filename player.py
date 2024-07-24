from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=-250)
        self.setheading(90)
        self.showturtle()


