from turtle import Turtle
FONT = ("Courier", 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def framing(self):
        self.goto(280,280)
        self.left(180)
        self.pendown()
        self.forward(560)
        self.penup()
        self.goto(-280,-260)
        self.left(180)
        self.pendown()
        self.forward(560)
        self.penup()

    def update_score(self):
        self.clear()
        self.goto(-200,240)
        self.write(f"Level: {self.level}", align= 'center', font= FONT)
    
    def level_up(self):
        self.level += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align= 'center', font= FONT)
