number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  # Sau if là một lệnh so sánh chứ không phải lệnh gán. sửa "if number % 2 = 0:" thành "if number % 2 == 0:"
  print("This is an even number.")
else:
  print("This is an odd number.")
