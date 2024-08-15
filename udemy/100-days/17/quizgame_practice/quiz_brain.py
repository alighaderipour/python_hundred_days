class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.len = len(q_list)
        self.score = 0
        self.questions_list = q_list

    def track_score(self, user_input, real_answer):
        if user_input == real_answer:
            self.score += 1
            return True
        else:

            return False

    def next_question(self):
        valid_answer = ["True", "False", "true", "false"]
        x = self.questions_list[self.question_number]
        y = input(f"Q.{self.question_number+1} : {x.text} ? ")
        if y.lower() in valid_answer:
            self.question_number += 1
            if self.track_score(y, x.answer):
                print(f"correct answer ! your score is : {self.score}")
            else:
                print(
                    f"wrong answer ! the correct answer was {x.answer}  ! your score is : {self.score}"
                )
        else:
            print('invalid answer ! choose "True" or "False"')

    def still_has_question(self):
        if self.question_number < self.len:
            return True
        else:
            print(f"Game Over ! your final score is {self.score}")
            return False
