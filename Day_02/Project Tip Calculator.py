bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number= int(input("How many people to split the bill? "))
cash = round((bill + bill*(tip / 100))/number , 2)
print(f"Each person should pay: $ {cash}")