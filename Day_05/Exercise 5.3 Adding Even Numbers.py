#Write your code below this row 👇
total_even = 0
for i in range(1, 101):
  if i % 2 == 0:
    total_even += i
print(total_even)

# Cách 2:
total_even2 = 0
for i in range(2, 101, 2):
  total_even2 += i
print(total_even2)