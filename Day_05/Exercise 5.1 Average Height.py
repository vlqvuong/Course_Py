# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

i = 0
height_total = 0

for height in student_heights:
  i += 1
  height_total += height
average_height = round(height_total / i)
print(f"Average height of students is: {average_height}")