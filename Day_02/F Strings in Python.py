print( 8 / 3)

print(int(8 / 3))
# chuyển từ float sang int chỉ lấy số nguyên của float chứ không làm tròn 2.59 bằng 3
# ta có code sau: round(number,n) trong đó number là số cần làm tròn, n là số chữ số bên phải dấu chấm động có nhập n dù là nhập 0 thì kết qur hàm round sẽ là float còn không nhập n thì kết quả sẽ được làm tròn về int

print(round((8 / 3) , 2))

print(round((8 / 3) , 1))

print(round(8 / 3))

print(8 // 3)
# kết quả cho ra khi thực hiện phép chia bằng "//" sẽ là 1 số int

# Ta có thể sử dụng a += 1 (tương đương với a + 1), tương tự với phép "-", "*", "/" sẽ thực hiện với giá trị của a phía trước hàng code đó

# F-string: combine các kiểu dữ kiệu khác nhau lại mà không cần chuyển đổi, cú pháp như sau 
a = 8 + 3
b = 1.8
c = True
print(f"text {a}, {b}, True or False? {c}")
# Các kiểu dữ liệu khác str muốn in mà không cần chuyển đổi thêm f trước str đó, và đặt các kiểu dữ liệu khác str vào cặp ngoặc nhọn {}

