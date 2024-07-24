from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(fun=player.move, key='Up')

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 285:
        player.goto(x=0, y=-280)
        scoreboard.update()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
