from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.got_to_start()
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def got_to_start(self):
        self.goto(STARTING_POSITION)


