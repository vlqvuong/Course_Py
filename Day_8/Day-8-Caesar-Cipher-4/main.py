alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
    # Nếu là decode thì shift sẽ âm để có thế lui ký tự trong list alphabet.
  for char in start_text:
    # Nếu trong text ta muốn decode hay encode có:dấu " ", ký tự hay số, thì ta giữ nguyên các ký tự, số và dấu cách đó.
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char     
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Xuất logo từ thư mục art bên ngoài main, sau đó in logo.
from art import logo
print(logo)
# Nếu ta muốn nhập "yes" để tiếp tục decode và "no" để dừng. thì tạo vòng lặp while, tạo biến continues = True, luôn đúng, và khi nhập "no" thì continues = False
continues = True
while continues:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
# nếu nhập shift lớn hơn 26 thì ta chia số đó cho 26 lấy số dư, thì số chia chia 26 lấy số dư sẽ từ 0 đến 25, nắm trong khoảng 0-26 nên sẽ không bị lỗi nữa.
  if shift > 26:
    shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restar = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  # nhập "yes" or "no" vào biến restar để tiếp tục hoặc dừng encode và decode.
  if restar == "no":
    continues = False
    print("Goodbye!")