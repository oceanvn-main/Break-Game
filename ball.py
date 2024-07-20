from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 2
        self.y_move = -2
        self.move_speed = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1.1
        self.move_speed *= 1.1

    def reset_position(self):
        random_potition = [-100, -200, -300, -50, -70, 60, 150, 200, 300]
        directions = [1, -1]
        self.x_move = 2 * random.choice(directions)
        self.y_move = 2 * random.choice([1])
        self.goto(x=random.choice(random_potition), y=-30)
        self.move_speed = 1
        self.bounce_y()

    def bounce_x(self):
        self.x_move *= -1
