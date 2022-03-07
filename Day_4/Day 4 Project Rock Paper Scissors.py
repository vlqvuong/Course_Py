rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game = [rock, paper, scissors]
your_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
if your_choose >=3 or your_choose < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game[your_choose])
  computer_choose = random.randint(0, 2)
  print(f"Computer choose:\n {game[computer_choose]}")
  if your_choose == 0 and computer_choose == 2:
    print("You win!")
  elif your_choose == 2 and computer_choose == 0:
    print("You lose!")  
  elif your_choose > computer_choose:
    print("You win!")
  elif your_choose < computer_choose:
    print("You lose!")  
  elif your_choose == computer_choose:
    print("It's a draw")