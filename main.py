import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

# TODO 5. Create a scoreboard
scoreboard = Scoreboard()

# TODO 2. Create and move the cars
car_manager = CarManager()

# TODO 1. Move the turtle with keypress
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # TODO 2.5 ....
    car_manager.create_car()
    car_manager.move()


    # TODO 3. Detect collision with  car
    for car in car_manager.all_cars:
        if car.distance(player.turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    # TODO 4. Detect when turtle reaches the other side
    if player.get_y() > 300:
        scoreboard.increase_scoreboard()
        player.increase_player_speed()
        player.reset_position()
        car_manager.level_up()


screen.exitonclick()