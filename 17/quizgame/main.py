from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q = Question(item["text"], item["answer"])
    question_bank.append(q)
print(question_bank)

q = QuizBrain(question_bank)
q.next_question()
