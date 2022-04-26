# file = open("data.txt")
# # Open data.txt file and save it inside a variable called file.
# contents = file.read()
# # read method returns the contents of that file as a string.
# print(contents)
# file.close()

with open("C:/Users/ADMIN/Desktop/data.txt") as file:
    # Move data.txt to Desktop & make code work again.
    contents = file.read()
    print(contents)

