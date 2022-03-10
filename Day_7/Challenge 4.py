# Step 4:

import random

stages = ['''
_+_______+
 |       |  
 0       |
/|\      |
/ \      |
         |
==========
''','''
_+_______+
 |       |  
 0       |
/|\      |
/        |
         |
==========
''','''
_+_______+
 |       |  
 0       |
/|\      |
         |
         |
==========
''','''
_+_______+
 |       |  
 0       |
/|       |
         |
         |
==========
''','''
_+_______+
 |       |  
 0       |
 |       |
         |
         |
==========
''','''
_+_______+
 |       |  
 0       |
         |
         |
         |
==========
''','''
_+_______+
 |       |  
         |
         |
         |
         |
==========
''']
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# TODO-1: Tạo 1 biến 'lives' để giữ số mạng còn lại.
# lives = 6

lives = 6

# Testing code:
print(f'Pssst, the solution is {chosen_word}.')

# create blank
display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for num in range(word_length):
        if chosen_word[num] == guess:
            display[num] = guess
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")
# TODO-2: Nếu từ đoán không phải là 1 từ trong chosen_word,
# Giảm lives 1.
# Nếu lives xuống còn 0 game dừng và in "You lose"
# join để gộp tất cả thành phần trong list thành 1 chuỗi.
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win")
        print(display)
    # TODO-3: in ASCII art từ 'stages' tương ứng với số lives còn lại
    print(stages[lives])

# Check guessed letter
# for position in range(word_length):
#     letter = chosen_word[position]
#     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter