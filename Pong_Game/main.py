from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Sasta Table Tennis")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)  # Increases ball's speed everytime it touches paddle
    screen.update()
    ball.move()

    # Ball's collision with the wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball's collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting the miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
