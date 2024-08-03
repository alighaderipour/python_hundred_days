from data import question_data
from question_model import Question
from quiz_brain import *

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

q = QuizBrain(question_bank)


while q.still_has_question():
    q.next_question()
