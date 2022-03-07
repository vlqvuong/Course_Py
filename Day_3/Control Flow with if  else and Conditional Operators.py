# Cấu trúc if / else :
# if condition:
#   do this
# else:
#   do this
# Lệnh sẽ kiểm tra điều kiện và nếu đáp ứng điều kiên sẽ thực thi các code sau dấu : sau điều kiện, còn nếu không đáp ứng điều kiện thì sẽ thực thi các code sau "else:"
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120: # không bao gồm 120, muốn có 120 thay dấu > bằng dấu >=
  print("You can ride the rollercoaster!")
else: # phải đặt else cùng vị trí tham chiếu tương ứng với if (vì else và if là 1 cặp)
  print("Sorry, you have to grow taller before you can ride.")
# > lớn hơn
# < bé hơn
# >= lớn hơn hoặc bằng
# <= bé hơn hoặc bằng
# == bằng với. khác với dấu = là gán giá trị vào 1 biến. dấu == so sánh 2 giá trị có bằng nhau không. không thể dùng dấu = trong lệnh if 
# != khác với