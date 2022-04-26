# Open the weather_data.csv and create a list named "data" contains the values frrom the .csv file
# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# csv library

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     # print(data)
#     # Create a csv.reader object, this object can be looped through
#     # Get each row inside this data:
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# Pandas Library: This is a python data analysis library. This is not a in-built, need to install to project
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
# pandas will read .csv file as an actual table
