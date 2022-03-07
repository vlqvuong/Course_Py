import random

test_seed = int(input("create a seed number: "))
random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# string.split(", ") chia string thành nhiều string và đặt vào chuỗi. các ký tự cách nhau bỏi dấu phẩy và dấu cách ", " sẽ được tách nhau ra
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

people = len(names)
people_pay = random.randint(0, people - 1)
name_people_pay = names[people_pay]
print(f"{name_people_pay} is going to buy the meal today!")



