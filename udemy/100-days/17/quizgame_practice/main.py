from data import question_data2
from question_model import Question
from quiz_brain import *

question_bank = []
# for item in question_data:
#     question = Question(item["text"], item["answer"])
#     question_bank.append(question)

for item in question_data2:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

q = QuizBrain(question_bank)


while q.still_has_question():
    q.next_question()
