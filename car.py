from turtle import Turtle
import random

COLORS = ['red', 'orange', 'purple', 'green', 'blue', 'violet']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.hideturtle()
        self.goto(random.randint(-280, 280), random.randint(-230, 230))
        self.showturtle()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(MOVE_INCREMENT)
