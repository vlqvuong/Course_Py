# Hàm len() không hoạt động cho kiểu Interger ở trong. EX: Len(12234) sẽ không cho kết quả
# Hàm len() cho kết quả là 1 số
# Vì vậy ta không thể thực hiện hàm sau:
# num_char = Len(Vuong)
# print("Your name has " + num_char + " character")
# Vì kiểu string không thể kết hợp với kiểu interger
num_char = len(input("What's your name?"))
new_num_char = str(num_char)
# str giúp chuyển kiểu int từ num_char sang kiểu Strings ở new_num_char
print("Your name has " + new_num_char + " character")
a = 123
# a hiện đang là kiểu interger
# Để chuyển sang kiểu String
str(a)
print(type(a))
# type(a) để biết xem a đang là kiểu gì
# Để chuyển a sang float
float(a)

