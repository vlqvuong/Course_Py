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

# # Pandas Library: This is a python data analysis library. This is not a in-built, need to install to project
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# # pandas will read .csv file as an actual table


# DataFrames & Series:
# A whole table is a dataframe in Pandas. Every single column is a series kind of like a list in Pandas

# import pandas
#
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# # Convert table data to dictionary.
#
# temp_list = data["temp"].to_list()
# # convert series "temp" yo list.
#
# # Average "temp"
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# # Use Series method to calculator average temp
#
# # Challenge: get maximum temp by use series method.
#
# print(data["temp"].max())
#
# # Get data in columns
#
# print(data["condition"])
# print(data.condition)

# Get Data in rows:

# print(data[data.day == "Monday"])
#
# # Pull out the row of data from weather data where the temp was maximum:
#
# # temp_max = data.temp.max()
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # Convert Monday's temperature to Fahrenheit
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # create a data frame from scratch:
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# # Create a .csv file from DataFrame was created from data_dict and then save it to new_data.csv.

# The Great Squirrel

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray" , "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")