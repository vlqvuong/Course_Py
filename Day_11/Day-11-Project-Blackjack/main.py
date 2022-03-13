############### Blackjack Project #####################

from art import logo
from replit import clear
import random

def add_card():
  """Phát lá bài ngẫu nhiên từ bộ bài và trả về card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def cal_score(cards):
  """Tính điểm từ bài của user hoặc computer"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    # Nếu có bài của user hoặc computer Blackjack, trả giá trị điểm của bài về không.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.appent(1)
    # Nếu có là Ace trong bài và điểm của bài lớn hơn 21 thì thay giá trị của Ace từ 11 thành 1. trả về giá trị điểm trong bài.
  return sum(cards)
  # Trả về giá trị của các là bài bên trong list

def compare_score(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You Went Over. You lose."

  if user_score == computer_score:
    return "You Draw"
  elif computer_score == 0:
    return "You Lose. Dealer has Blackjack"
  elif user_score == 0:
    return "You Win With a Blackjack"
  elif user_score > 21:
    return "You Went Out. You Lose"
  elif computer_score > 21:
    return "Dealer Went Out. You Win"
  elif user_score > computer_score:
    return "You Win"
  else:
    return "You Lose"

def blackjack_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  continues = True

  for i in range(2):
    user_cards.append(add_card())
    computer_cards.append(add_card())

  while continues:
    user_score = cal_score(user_cards)
    computer_score = cal_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      continues = False
      # Nếu User, Computer Blackjack và điểm của user > 21 thì kết thúc game.
      
    else:
      user_add = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_add == "y":
        user_cards.append(add_card())
      else:
        continues = False
    # Nếu User muốn add thêm bài và bài của user chưa trên 21 điểm thì add thêm còn không thì qua bước kế tiếp.

  # Nếu lượt của user kết thúc thì đến lượt computer. Nếu bài Computer dưới 17 điểm thì tiếp tục rút bài.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(add_card())
    computer_score = cal_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack_game()
# Khi người chơi muốn chơi nữa thì nhập "y" màn hình sẽ được làm sạch và vòng lặp blackjack_game sẽ bắt đầu lại 1 lần nữa. Nếu muốn ngừng thì nhập "n"