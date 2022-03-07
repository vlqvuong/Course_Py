# and:
# ex: a and b đúng chit khi cả a và b đều đúng
# ví dụ:
# a = 10
# kq = a < 12 and a > 5
# print(kq)
# kq hiện là True vì a = 10 < 12, và a = 10 > 5 đều đúng
# a = 10
# kq = a > 12 and a > 5
# print(kq)
# kq hiện là False vì a = 10 > 12 là sai, và a = 10 > 5 đúng

# or: C or D
# True khi C hoặc D True. False khi cả C và D False

# not: not E
# đảo ngược E, nếu E là True thì not E là False và ngược lại
# Ex:
# a = 10
# kq = not a > 12
# print(kq)
# kq = True vì a = 10 > 12 là False

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Children tickets are ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"Younth tickets are ${bill}.")
  elif age >= 45 and age <= 55:
    print(f"Middle-aged ticket are ${bill}")
  else:
    bill = 12
    print(f"Adult tickets are ${bill}.")
  photo = input("Do you want to take a photo? Y or N? ")
  if photo == "Y":
    bill += 3 #tương đương với code sau: bill = bill + 3
# không có else đồng nghĩa với việc khi điều kiện sai sẽ không thực thi lệnh nào cả
  print(f"Your final bill is ${bill}")
else: 
  print("Sorry, you have to grow taller before you can ride.")
