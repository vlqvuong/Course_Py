# import another_module
#
# print(another_module.another_variable)
#
# import turtle
# timmy = turtle.Turtle()
# # Lấy 1 Class từ module turtle.

# # Có thể viết lại như sau:
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSalmon")
# timmy.forward(100)
# # Để truy cập attribute của object dùng cú pháp sau:
# # object.attribute.
# my_screen = Screen()
# print(my_screen.canvheight)
# # Để truy cập đến method của object cũng bằng cách tương tự như truy cập attribute.
# my_screen.exitonclick()

# install package into our project use pypi.
# import prettytable
# In order to see the sourse code: right click and then click Go TO and click implementation.

from prettytable import PrettyTable

# Create a PrettyTable object and save it to a variable called table

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Chamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# Change attribute align from "c" (centre align) to "l" (left align)
table.align = "l"

print(table)