#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# rand.seed(a) với mỗi số a sẽ cho 1 số random cố định
rand_int = random.randint(0, 1)
if rand_int == 0:
  print("Heads")
elif rand_int == 1:
  print("Tails")








