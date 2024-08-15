from turtle import Turtle
import random

FOOD_SIZE = 0.75


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

