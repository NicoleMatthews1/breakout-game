from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block_manager import BlockManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Breakout")

screen.tracer(0)

paddle = Paddle((0, -350))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")

block_manager = BlockManager()

block_manager.add_rows()


running = True

while running:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()


    # Detect collision with top wall
    if ball.ycor() > 380:
        ball.bounce_y()

    # Detect collision with right wall
    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.ycor() < -320 and ball.distance(paddle) < 125:
        ball.bounce_y()

    # Detect collision with bottom wall
    if ball.ycor() < -350:
        ball.reset_position()
        scoreboard.update_lives()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            running = False

    # collision
    for block in block_manager.blocks:
        if block.distance(ball) < 30:
            block_manager.blocks.remove(block)
            block.reset()
            scoreboard.update_score()
            ball.bounce_y()

    if block_manager.blocks == []:
        scoreboard.you_win()
        running = False

















screen.exitonclick()