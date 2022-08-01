import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen options
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('lightgreen')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Drawing start and finish lines
scoreboard.framing()

# Game process
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.framing()
    # cars movement
    car_manager.create_car()
    car_manager.move_cars()

    # Keyboard 
    screen.listen()
    screen.onkeypress(player.move, 'Up')

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Sucessful crossing
    if player.ycor() >= 280:
        scoreboard.level_up()
        scoreboard.update_score()
        car_manager.increase_car_speed()
        player.replace()

screen.exitonclick()