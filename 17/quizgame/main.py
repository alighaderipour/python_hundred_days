from data import question_data
from question_model import Question

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

for item in question_bank:
    print(item.text, item.answer)
