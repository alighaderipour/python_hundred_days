class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        x = self.questions_list[self.question_number]
        input(f"q.{self.question_number} : {x.text} ? ")
