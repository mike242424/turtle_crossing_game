from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard

TIME = 0.3

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = []
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(fun=turtle.move, key='Up')

while game_is_on:
    time.sleep(TIME)
    screen.update()
    car = Car()
    cars.append(car)

    for car in cars:
        car.move()

    if turtle.ycor() > 285:
        turtle.goto(x=0, y=-280)
        scoreboard.update()

    for car in cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
