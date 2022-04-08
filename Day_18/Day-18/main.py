# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")

# Challenge 1: Draw a dashed line:Draw a square:
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Right click on variable-> refactor-> rename -> type the name want to change

# Challenge 2: Draw a dashed line:

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3: Drawing Different Shapes: Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon and decagon. Each shape with a random difference in color

# i = 3
# colors = ["black", "medium blue", "gold", "sienna", "hot pink", "indigo", "dark slate blue", "medium purple"]
# while i <= 10:
#     angle = 360 / i
#     tim.pencolor(random.choice(colors))
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(angle)
#     i += 1

# Challenge 4: Generate a Random Walk

# directions = [0, 90, 180, 270]
# colors = ["black", "blue", "gold", "green", "red", "gray", "yellow", "medium purple"]
#
# tim.speed("fastest")
# tim.pensize(10)
# for i in range(200):
#     tim.pencolor(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     # Random direction in directions list: 0-east, 90-north, 180-west, 270-south
#
# screen = Screen()
# screen.exitonclick()

# Python Tuples:
# You can't change the values in tuples

# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# directions = [0, 90, 180, 270]
# colors = ["black", "blue", "gold", "green", "red", "gray", "yellow", "medium purple"]
#
# tim.speed("fastest")
# tim.pensize(10)
#
# for i in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     # Random direction in directions list: 0-east, 90-north, 180-west, 270-south

# Challenge 4: Draw a Spirograph

import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(angle):
    for i in range(int(360 / angle)):
        tim.pencolor(random_color())
        tim.circle(70)
        tim.setheading(tim.heading() + angle)

spirograph(5)

screen = t.Screen()
screen.exitonclick()
