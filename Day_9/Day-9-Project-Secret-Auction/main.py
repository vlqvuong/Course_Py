from replit import clear
from art import logo
print(logo)
# In logo của Secret Auction.
secret_auction = {}
finished = False

def find_highest(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bid = bidding_record[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
# Tạo hàm tìm số lớn nhất trong số các người đấu giá.
while not finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  secret_auction[name] = price
  # Nhập tên, giá đấu giá, sao đó cho vào dictionary với key là tên, giá là value.
  continues = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if continues == "yes":
    clear()
  elif continues == "no":
    finished = True
    find_highest(secret_auction)
