from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["question"]  # stored in variable to prevent typo errors
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)  # Question("A slug", "True")
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

percent = round(quiz.score / len(quiz.question_list) * 100, 2)
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score} / {len(quiz.question_list)}, {percent}% in percentage.")
