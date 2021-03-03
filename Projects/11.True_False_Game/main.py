from question_model import Question
from data1 import question_data
from quiz_brain import QuizBrain
question_bank =  []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You complete the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")