COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle, speed
import random

class CarManager(Turtle):
    
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.add_car()

    def create_car(self):
        random_chance = random.randint(1,7)
        if random_chance == 6:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            random_y = random.choice(range(-240,270))
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def increase_car_speed(self):
        self.speed += MOVE_INCREMENT

    def add_car(self):
        works = random.choice([True, False])
        if works:
            new_car = self.create_car()
            self.cars.append(new_car)
            self.goto(300, (random.choice(range(-240,280))))

    

    
