import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code:
print(f'Pssst, the solution is {chosen_word}.')

# create blank
display = []
for _ in range(word_length):
    display += "_"
print(display)

# TODO-1: sử dụng vòng lặp while để đoán chữ tiếp tục. Vòng lặp chỉ dừng khi đã đoán tất cả các chữ trong chosen_word và list 'display' không còn khoản trống "_". Sau đó có thể kết thúc và nói đã thắng.
    
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     for num in range(word_length):
#         if chosen_word[num] == guess:
#             display[num] = guess
# print("You Win")
# print(display)

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()
    for num in range(word_length):
        if chosen_word[num] == guess:
            display[num] = guess
    if "_" not in display:
        end_game = True
        print("You Win")
        print(display)

# Check guessed letter
# for position in range(word_length):
#     letter = chosen_word[position]
#     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter