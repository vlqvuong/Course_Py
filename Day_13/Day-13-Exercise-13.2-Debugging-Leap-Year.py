year = int(input("Which year do you want to check?"))
# Year ở đây được nhập vào với dàng String, không thực hiện phép chia được. Khi chạy sẽ xuất hiện dòng mã lỗi sau: TypeError: not all arguments converted during string formatting. Để thực hiện được ta dùng cách sau, chuyển year từ kiểu string sang integer.

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")