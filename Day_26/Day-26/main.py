"""
# List Comprehension: new_list = [new_item for item in list]
# Create a new list from numbers and add 1 to each value by use list comprehension.
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Vuong"
letters_list = [letter for letter in name]
print(letters_list)
# new_list contain whole letter in name. ['V', 'u', 'o', 'n', 'g']

# Challenge: create a new list from a range and double the value in the range
double_range = [n * 2 for n in range(1, 5)]
print(double_range)

# Conditional List Comprehension: new_list = [new_item for item in list if test]
names = ["Vuong", "Quynh", "Tam", "An", "Hai", "Quoc", "Dung"]
# Create a list contain the names less than 5 letter from names list.
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Create a list contains the names longer than 5 characters in all caps
long_name = [name.upper() for name in names if len(name) >= 5]
print(long_name)
"""


"""
# Exercise 1:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should
# contain every number in the list numbers but each number should be squared

squared_numbers = [number * number for number in numbers]
print(squared_numbers)
"""


"""
# Exercise 2:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# You are going to write a List Comprehension to create a new list called result. This new list should only contain
# the even numbers from the list numbers:
result = [number for number in numbers if number % 2 == 0]
print(result)
"""


# Dictionary Comprehension: new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key:value) in dict.items()}
# new_dict = {new_key:new_value for (key:value) in dict.items() if test}


"""
names = ["Vuong", "Quynh", "Tam", "An", "Hai", "Quoc", "Dung"]
# Create a new dictionary with key is name in names list and value is random score from 1 to 100:
import random
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

# Create a dictionary containing students who have a score of 60 or over
# print(students_score.items())
passed_students = {key: value for (key, value) in students_score.items() if value >= 60}
print(passed_students)
"""


"""
# Exercise 4:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the
# given sentence and calculates the number of letters in each word.
# Don't change code above 👆

# Write your code below:

result = {word:len(word) for word in sentence.split()}
# use the split() method to split each word on a string

print(result)
"""


"""
# Exercise 5:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:

weather_f ={day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
"""


