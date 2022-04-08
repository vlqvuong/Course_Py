# from turtle import Turtle, Screen
#
# vuong = Turtle()
# screen = Screen()
#
#
# # Python Higher Order Functions & Event Listeners
# def move_forwards():
#     vuong.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

# Make an Etch-A-Sketch App
from turtle import Turtle, Screen

vuong = Turtle()
screen = Screen()


def move_forwards():
    vuong.forward(10)


def move_backwards():
    vuong.backward(10)


def turn_left():
    new_heading = vuong.heading() + 10
    vuong.setheading(new_heading)


def turn_right():
    new_heading = vuong.heading() - 10
    vuong.setheading(new_heading)


def clear_drawing():
    vuong.reset()
    # Reset all Turtles on the Screen to their initial state.


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
