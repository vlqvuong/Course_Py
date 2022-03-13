4 + 5 # Phép cộng 
6 - 4 # Phép Trừ
6 * 6 # Phép Nhân
6 / 3 # Phép Chia, phép chia luôn cho kết quả là kiểu Float, dù cho kết quả là số nguyên
2 ** 4 # Lũy thừa 2 mũ 4
print(3 * 3 + 3 / 3 - 3) # Kết quả là 7.0
# Trong Python thứ tự ưu tiên các phép toán là:
# ()
# **
# * /
# + - 
# Để có kết quả là 3.0 dùng code sau
print(3 * (3 + 3) / 3 - 3)