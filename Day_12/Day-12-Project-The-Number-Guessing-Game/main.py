import random
from art import logo
print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
print(answer)
# Tạo 1 số ngẫu nhiên từ 1 đến 100.

def check_guess(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
# Kiểm tra xem số đoán lớn hơn hay nhỏ hơn, nếu đoán sai giảm 1 lượt
def level_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
  if level == "hard":
    return HARD_LEVEL_TURNS
  elif level == "easy":
    return EASY_LEVEL_TURNS
# Kiểm tra Level muốn chơi, easy có 10 lượt, hard có 5 lượt
def game():
  turns = level_difficulty()
  game_continues = True
  while game_continues:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    if guess != answer and guess > 0:
      turns = check_guess(guess, answer, turns)
    elif guess == 0:
      print("You've run out of guesses, you lose.")
      game_continues = False
    elif guess == answer:
      print(f"You got it! The answer was {answer}.")
      game_continues = False

game()
