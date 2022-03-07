
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
