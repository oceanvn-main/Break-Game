from turtle import Screen, Turtle
import random
import time
import turtle
from paddle import Paddle
from ball import Ball
from Score_board import Scoreboard
from wall_manager import WallManager

screen = Screen()
screen.setup(width=1600, height=1000)
screen.bgcolor('black')
screen.title("Welcome to Break Game")
screen.tracer(0)

score = Scoreboard()
wall_manager = WallManager(screen_width=1600, screen_height=1000)
all_walls = wall_manager.create_all_walls()
ball = Ball()
position = (-200, -430)
paddle = Paddle(position)


def check_collision_with_paddle(ball, paddle):
    ball_radius = 10
    ball_left = ball.xcor() - ball_radius
    ball_right = ball.xcor() + ball_radius
    ball_top = ball.ycor() + ball_radius
    ball_bottom = ball.ycor() - ball_radius

    paddle_width = paddle.shapesize()[1] * 20
    paddle_height = paddle.shapesize()[0] * 20
    paddle_left = paddle.xcor() - paddle_width / 2
    paddle_right = paddle.xcor() + paddle_width / 2
    paddle_top = paddle.ycor() + paddle_height / 2
    paddle_bottom = paddle.ycor() - paddle_height / 2

    if paddle_left < ball_right and ball_left < paddle_right and paddle_bottom < ball_top and ball_bottom < paddle_top:
        hit_position = (ball.xcor() - paddle.xcor()) / (paddle_width / 2)
        angle = hit_position * 45
        ball.setheading(180 - angle)
        return True
    return False


def check_collision_with_wall(ball, wall):
    ball_left = ball.xcor() - 10
    ball_right = ball.xcor() + 10
    ball_top = ball.ycor() + 10
    ball_bottom = ball.ycor() - 10

    wall_left = wall.xcor() - wall.shapesize()[1] * 10
    wall_right = wall.xcor() + wall.shapesize()[1] * 10
    wall_top = wall.ycor() + wall.shapesize()[0] * 10
    wall_bottom = wall.ycor() - wall.shapesize()[0] * 10

    if wall_left < ball_right < wall_right and wall_bottom < ball_top < wall_top:
        return True
    if wall_left < ball_left < wall_right and wall_bottom < ball_bottom < wall_top:
        return True
    return False


is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    screen.listen()
    screen.onkey(paddle.move_right, "d")
    screen.onkey(paddle.move_left, "a")
    time.sleep(0.01)

    # Detect ball over the wall
    if ball.ycor() > 440 or ball.ycor() < -440:
        ball.reset_position()

    # Detect collision with walls
    for wall in all_walls:
        if check_collision_with_wall(ball, wall):
            ball.bounce_y()
            wall.hideturtle()
            all_walls.remove(wall)
            score.point()

    # Detect collision with paddle
    if check_collision_with_paddle(ball, paddle):
        ball.bounce_y()

    # Detect collision with right or left
    if ball.xcor() < -780 or ball.xcor() > 780:
        ball.bounce_x()

    # Detect paddle misses
    if ball.ycor() < -430:
        ball.reset_position()

    if len(all_walls) == 0:
        score.game_over()
        is_game_on = False

screen.update()
screen.mainloop()
