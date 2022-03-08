# 5.2 Using the "for loop" with Python Lists
fruits = ["Apple", "Peach", "Pear"]
# for item in list:
# Vòng lặp for gán lần lượt mỗi biến trong list vào 1 biến item mà ta cần gán. Trong list có tổng cộng bao nhiêu biến thì vồng lặp thực hiện thay giá trị biến item bấy nhiêu lần.
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
# ta có thể làm bất cứ thứ gì với biến tạm thời bên trong vòng lặp for.
# Các dòng lệnh phía dưới dòng lặp for sẽ thực hiện ở mỗi vòng với điều kiện nó cách vào bên dưới vòng lặp for, nếu đặt bằng với vòng lặp for thì khi vòng lặp hoàn tất mới thực hiện dòng code đó.
# Có thể sử dụng vòng lặp for để tính tổng giá trị trong list thay cho hàm sum(): sum(list)
# Hàm max(), min(): tìm số có giá trị lớn nhất, nhỏ nhất trong list: max(list), min(list)

# 5.5 for loop and the range() function:
# Vòng lặp for còn có thể dùng bằng cách tạo 1 khoảng rồi chạy vòng for bằng hàm range()
# Ex: for number in range(a, b) chạy vòng lặp for trong khoảng a:b-1 thay vì dùng list.
for number in range(1, 10):
  print(number)
# Hàm range(a,b) tạo 1 dãy số từ a đến b-1.
# step của range(a, b, step) nghĩa là các số trong range bây giờ sẽ là: a, a+step, a+step+step,... b-1
# Tính tổng từ 1-100
total = 0
for number in range(1, 101):
  total += number
print(total)