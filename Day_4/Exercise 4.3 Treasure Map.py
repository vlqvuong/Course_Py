# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# x = int(position[1])
# y = int(position[0])
# if x == 1:
#   row1[y - 1] = "X"
# elif x == 2:
#   row2[y - 1] = "X"
# else:
#   row3[y - 1] = "X"

horizonal = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical - 1] 
# # Chọn hàng để thay X
# selected_row[horizonal - 1] = "X"
# # Chọn cột thay X
# # Hoặc có thể dùng code sau:
map[vertical - 1][horizonal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")