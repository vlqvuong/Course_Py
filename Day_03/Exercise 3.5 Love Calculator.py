# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# lower() function: chuyển tất cả các chữ về chữ thường. Cách dùng:
# name = Vo Le Quoc Vuong
# name.lower()
# Bây giờ name sẽ là: vo le quoc vuong

# count() function: đếm các ký tự có trong chuỗi(string). Cách dùng:
# name.count("v") (name = Vo Le Quoc Vuong) kết quả là 0 vì: V khác v
# name.count("v") (name = vo le quoc vuong) kết quả là 2


#Write your code below this line 👇

name1_lower = name1.lower()

name2_lower = name2.lower()

name_total = name1_lower + name2_lower

count_T = name_total.count("t")
count_R = name_total.count("r")
count_U = name_total.count("u")
count_E = name_total.count("e")
true_score = str(count_T + count_R + count_U + count_E)

count_L = name_total.count("l")
count_O = name_total.count("o")
count_V = name_total.count("v")
count_E = name_total.count("e")
love_score = str(count_L + count_O + count_V + count_E)

true_love_score = int(true_score + love_score)

if true_love_score < 10 or true_love_score > 90:
  print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score >= 40 and true_love_score <= 50:
  print(f"Your score is {true_love_score}, you are alright together.")
else:
  print(f"Your score is {true_love_score}.")