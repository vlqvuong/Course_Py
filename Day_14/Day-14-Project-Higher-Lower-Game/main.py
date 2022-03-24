from game_data import data
from art import logo, vs
import random
from replit import clear

def random_choosen():
  """Ngẫu nhiên chọn 1 dictionary trong game_data để tiến hành so sánh"""
  return random.choice(data)
# chọn ngẫu nhiên 1 dictionary ra để làm phép so sánh

def print_choosen(rand_dictionary):
  name = rand_dictionary.get("name")
  description = rand_dictionary.get("description")
  country = rand_dictionary.get("country")
  return f"{name}, a {description}, from {country}."
# Function Trả kết quả thuộc tính trong các vế

def print_game():
  print(f"Compare A: {print_choosen(dictionary_a)}")
  print(vs)
  print(f"Against B: {print_choosen(dictionary_b)}")
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  return guess
  
dictionary_a = random_choosen()
dictionary_b = random_choosen()
if dictionary_a == dictionary_b:
  dictionary_b = random_choosen()
game_end = False
score = 0
print(logo)
guess = print_game()

while not game_end:
  follower_a = dictionary_a.get("follower_count")
  print(follower_a)
  follower_b = dictionary_b.get("follower_count")
  print(follower_b)
  if guess == "A":
    if follower_a > follower_b:
      dictionary_a = dictionary_b
      dictionary_b = random_choosen()
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      guess = print_game()
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_end = True
  elif guess == "B":
    if follower_b > follower_a:
      dictionary_a = dictionary_b
      dictionary_b = random_choosen()
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      guess = print_game()
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_end = True
