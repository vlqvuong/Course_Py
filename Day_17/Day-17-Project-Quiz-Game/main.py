# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank = []
#
# for dictionary in question_data:
#     text = dictionary.get("text")
#     answer = dictionary.get("answer")
#     question_bank.append(Question(text, answer))
# # Create a Question object from each entry in question_data
# # Append each Question object to the question_bank
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    text = dictionary.get("question")
    answer = dictionary.get("correct_answer")
    question_bank.append(Question(text, answer))
# Create a Question object from each entry in question_data
# Append each Question object to the question_bank

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")