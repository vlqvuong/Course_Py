# Caculator

# Add
def add(n1, n2):
  return n1 + n2

# Subtract

def subtract(n1, n2):
  return n1 - n2

# Multiply

def multiply(n1, n2):
  return n1 * n2

# devide

def devide(n1, n2):
  return n1 / n2

calculator = {}
calculator["+"] = add
calculator["-"] = subtract
calculator["*"] = multiply
calculator["/"] = devide
def calculator():
  num1 = int(input("What's the first number?: "))
  # Tạo vòng lặp và in mỗi ký tự phép toán trong dictionary caculator:
  for symbol in calculator:
    print(symbol)
  continues = True
  while continues:
    calculator_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    function = calculator[calculator_symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {calculator_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower() == "y":
      num1 = answer
    else:
      continues = False
      calculator()

calculator()
