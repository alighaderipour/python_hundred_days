from main import *


class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.questions_list = question_bank

    def next_question(self):
        pass


quizbrain = QuizBrain
print(quizbrain.questions_list)
