import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")

player = Player()
car = CarManager()
scoreboard = Scoreboard()
car_list = []
screen.listen()

screen.onkey(player.go_up, "Up")

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

    # Turtle move pass level:
    if player.at_finish_line():
        car.level_up()
        scoreboard.increase_level()

    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


