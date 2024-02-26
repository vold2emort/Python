from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for data in question_data:
#     question_bank.append(Question(data["text"], data["answer"]))

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"you final score was: {quiz.score}/{quiz.question_number}")
