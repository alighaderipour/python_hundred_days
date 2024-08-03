class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.len = len(q_list)
        self.score = 0
        print(self.len, "self.len")
        self.questions_list = q_list

    def track_score(self, user_input, real_answer):
        if user_input == real_answer:
            self.score += 1
        else:
            print(f"your answer was wrong. correct answer was {real_answer}")

    def next_question(self):
        x = self.questions_list[self.question_number]
        y = input(f"q.{self.question_number} : {x.text} ? ")
        self.track_score(y, x.answer)
        self.question_number += 1
        print(self.score)

    def still_has_question(self):
        if self.question_number < self.len:
            return True
        else:
            print(f"your score is {self.score}")
            return False
