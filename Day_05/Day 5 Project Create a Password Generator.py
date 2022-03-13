#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for letter in range(1, nr_letters + 1):
#   password += random.choice(letters)
#   # random.choice(list) chọn ngẫu nhiên trong list.
# for symbol in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
# for number in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Phải tạo 1 list rồi xáo trộn vị trí thứ tự các ký tự trong list.

password_list = []

for letter in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)
# Xáo trộn ngẫu nhiên các item trong list

password = ""

for char in password_list:
  password += char

print(password)
