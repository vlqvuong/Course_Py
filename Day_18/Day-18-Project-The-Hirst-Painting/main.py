# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# list_color = []
# # list_color.append(color[0].rgb)
# for color in colors:
#     # r = color.rgb[0]
#     r = color.rgb.r
#     g = color.rgb[1]
#     b = color.rgb[2]
#     tuple_color = (r, g, b)
#     list_color.append(tuple_color)
#
# print(list_color)
# code in upper to create a list of colors bellow
import turtle as t
import random

vuong = t.Turtle()
t.colormode(255)

list_color = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50),
              (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11),
              (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26),
              (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127),
              (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100),
              (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165),
              (25, 91, 65), (172, 205, 180)]
vuong.speed("fastest")
vuong.penup()
vuong.hideturtle()
vuong.setheading(225)
vuong.forward(300)
vuong.setheading(0)
number_of_dot = 100
for dot_count in range(1, number_of_dot + 1):
    vuong.dot(20, random.choice(list_color))
    vuong.forward(50)
    if dot_count % 10 == 0:
        vuong.setheading(90)
        vuong.forward(50)
        vuong.setheading(180)
        vuong.forward(500)
        vuong.setheading(0)

screen = t.Screen()
screen.exitonclick()