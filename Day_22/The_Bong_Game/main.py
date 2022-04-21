# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong Game")
# screen.tracer(0)
#
# # Create a Paddle that responds to Key Presses
# paddle = Turtle()
# paddle.penup()
# paddle.goto(350,0)
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
#
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# screen.listen()
#
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")
#
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#
# screen.exitonclick()

# Write the Paddle Class and Create the Second Paddle


# import time
# from turtle import Turtle, Screen
# from paddle import Paddle
# from ball import Ball
#
# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong Game")
# screen.tracer(0)
#
# # Create a Paddle that responds to Key Presses
# # paddle = Turtle()
# # paddle.penup()
# # paddle.goto(350,0)
# # paddle.shape("square")
# # paddle.color("white")
# # paddle.shapesize(stretch_wid=5, stretch_len=1)
# #
# #
# # def go_up():
# #     new_y = paddle.ycor() + 20
# #     paddle.goto(paddle.xcor(), new_y)
# #
# #
# # def go_down():
# #     new_y = paddle.ycor() - 20
# #     paddle.goto(paddle.xcor(), new_y)
#
#
# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
#
#
# screen.listen()
#
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     ball.move()
#
#
# screen.exitonclick()

# Add the Ball Bouncing Logic
#
#
# import time
# from turtle import Turtle, Screen
# from paddle import Paddle
# from ball import Ball
#
# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong Game")
# screen.tracer(0)
#
#
# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
#
#
# screen.listen()
#
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     ball.move()
#
#     # Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         ball.bounce()
#
#
# screen.exitonclick()


# How to Detect Collisions with the Paddle


import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with baddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the Ball goes Out of Bounds:
    # Detect R paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
