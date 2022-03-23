# Debugging. 
# Vài tips và phương pháp để phát hiện và loại bỏ Bug.

# 1. Describe the problem

############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# What is the for-loop doing? for-loop đang là vòng lặp i trong range(1,20) sau đó kiểm tra i có bằng 20 không, nếu có thì thực hiện lệnh in "You got it" ra.
# When is the function meant to print "You got it"? Function my_function() in "You got it" khi vòng lặp lặp đến giá trị i=20, và lệnh if i==20 đúng thì lệnh in trong if sẽ được thực thi.
# What assumptions are you making about the value of i? Giá trị của i sẽ là từ 1 đến 19 vì hàm range(i,j) chạy từ i,... đến (j-1)
# Để làm cho in ra được dòng đó thì đơn giản chỉ cần sửa số 20 trong hàm range thành 21

# # Reproduce the Bug: Các Bug chỉ xuất hiện khi lặp đi lặp lại nhiều lần
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# # Vì dice_num được lấy random từ 1-6 mà số thứ tự trong list dice_imgs là bắt đầu từ 0 và kết thúc ở 5, nên khi hàm randint cho ra số 6 thì trong list không có giá trị đó để in ra

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# # Khi nhập năm 1994 thì không có điều kiện nào thõa mãn vậy nên sẽ không in ra bất cứ thứ gì cả. Để fix Bug này chỉ đơn giản thêm điều kiện = ở vế if hay elif đều được.

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# # Có những lỗi sẽ hiện ngay khi chúng ta viết chương trình, có những lỗi chỉ hiện tỏng khi chạy (vì ta sử dụng hàm inout thì khi chạy ta mới nhập vào). Ngoài ra còn có những Bug thuộc về kiến thức trải nghiệm qua rồi mới biết cách Fix.
# # Ở đây có 3 lỗi lần lượt như sau:
#  +Lỗi đầu tiên là hàm if không thực thi lệnh gì vì hàm print() nằm cùng cấp với nó, để giải quyết thì cần thụt hàng hàm print vào.
#  +Lỗi thứ 2 thuộc về lỗi khi nhập hàm vào input(). Già trị mặc định khi nhập giá trị vào hàm input là str, nếu muốn thực hiện phép toán so sánh thì phải đổi kiểu str sang int hoặc float (nếu muốn so sánh số thập phân).
#  + Lỗi thứ 3 là khi in sẽ in y nguôn trong lệnh print ra và máy tính sẽ không phát hiện ra lỗi gì vì code của chúng ta đang đúng. Nhưng kết quả ta muốn in ra lại là số tuổi ta nhập vào. Trường hợp này thì kiến thức về FString sẽ giúp ta. Nếu ta chưa biết về hàm String thì sẽ không thể giải quyết được trường hợp này.
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# # Ở đây word_per_page được so sánh với giá trị nhập vào hàm input chứ giá triị khi ta nhập vào không gán được giá trị hàm input nhập vào nên phép toán không được thực hiện. Ở đây máy sẽ so sánh giá trị của hàm input nhập vào và giá trị của biến word_per_page rồi cho kết quả là True or False (1 or 0). Để fix ta sửa lại 2 dấu == thành 1 dấu =.
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# Chèn new_item chỉ thực hiện khi kết thức vòng lặp for cho nên chỉ khi kết thúc for nó mới được thêm vào, lúc này new_item = 13 * 2 = 26. Muốn fix ta để dòng thêm ký tự new_item vào trong vòng lặp for là được [2, 4, 6, 10, 16, 26]
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# Tips 7: Hãy nghỉ ngơi 1 lát để cho mắt được thư giản rồi vào tìm Bug tiếp.

# Tips 8: Nói chuyện, gặp bạn bè ngoài đời.

# Tips 9: Đừng quên chạy code của bạn thường xuyên để biết lỗi gần nhât diễn ra từ khi nào. Chạy để biết những gì bạn đã viết có đúng với những gì bạn mong muôn hay không.

# Tips 10: Ask StackOverflow