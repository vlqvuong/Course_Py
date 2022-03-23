# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Lỗi ở đây là lệnh if đầu tiên phải là And chứ không phải or. Vì khi đó sẽ trùng với lệnh if ở dưới.
# Khi fix lỗi 1 thì lỗi 2 vẫn còn do các vòng if riêng rẻ, nếu số chia hết cho cả 3 và 5, số đó sẽ được so sánh thêm 2 lần nữa và tổng cộng in kết quả ra 3 lần Fizz Buzz FizzBuzz. Code được fix lại như sau:

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)