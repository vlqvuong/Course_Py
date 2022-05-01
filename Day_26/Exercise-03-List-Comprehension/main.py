with open("file1.txt") as file_1:
    list_1 = file_1.readlines()
with open("file2.txt") as file_2:
    list_2 = file_2.readlines()

result = [int(num) for num in list_1 if num in list_2]

# Write your code above 👆

print(result)


