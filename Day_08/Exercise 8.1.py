#Write your code below this line 👇
import math
# Để truy cập các hàm toán học trong math.
def paint_calc(height, width, cover):
    number_of_can = math.ceil(height * width / cover)
    # Hàm ceil(x) trong math "x" là số thập phân giúp trả giá trị về số nguyên gần nhât lớn hơn x
    print(f"You'll need {number_of_can} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)