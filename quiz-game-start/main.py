from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
import sys
sys.path.insert(0,'<project directory>')
question_bank = []
for question1 in question_data:
    question_text = question1["text"]
    question_answer = question1["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")