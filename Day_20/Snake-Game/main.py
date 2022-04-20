# import time
# from turtle import Screen, Turtle
#
# screen = Screen()
# screen.setup(width=600, height=600)
# # Set up a screen 600x600
# screen.bgcolor("black")
# # Change screen's background color to black
# screen.title("Snake Game")
# # Set title of turtle_window
# screen.tracer(0)
# # Turns turtle animation on or off and set delay for update drawings
#
#
# snakes = []
# position = [(0, 0), (-20, 0), (-40, 0)]
# for i in position:
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(i)
#     snakes.append(snake)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     # Update screen when all squares forward 20 pixel
#     time.sleep(0.1)
#     # Delay execution for a given number of second
#
#     for snake_num in range(len(snakes)-1, 0, -1):
#         # for loop in range(start=len(snakes)-1, stop=0, step=-1)
#         new_x = snakes[snake_num - 1].xcor()
#         new_y = snakes[snake_num - 1].ycor()
#         snakes[snake_num].goto(new_x, new_y)
#         # The square of the snake will go to the position of the in front square
#     snakes[0].forward(20)
#     # The direction of movement of the first square of the snake
#
# screen.exitonclick()

# Continue the snake game with OOP

import time
from turtle import Screen, Turtle
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.snake_move()

