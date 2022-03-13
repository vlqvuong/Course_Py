
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5 for ticlet.")
  elif age <= 18:
    print("Please pay $7 for ticket.")
  elif age <= 22:
    print("Please pay $10 for ticket.")
  else:
    print("Please pay $12 for ticket.")
else: 
  print("Sorry, you have to grow taller before you can ride.")
Cấu trúc if/elif/else:
# if condition 1:
#   Do A
# elif condition 2:
#   Do B
# else:
#   Do C
# chúng ta có thể sùng nhiều elif để kiểm tra nhiều điều kiện, khi nào hết điều kiện, những cái không thõa mãn điều kiện sẽ thực thi các code trong "Do C"