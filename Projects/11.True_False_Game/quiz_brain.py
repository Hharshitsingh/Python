class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_answer = self.question_list[self.question_number]
        correct_answer = current_answer.answer
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, u_answer, c_answer ):
        if c_answer.lower() == u_answer.lower():
            self.score += 1 
            print("Right Answer")
            print(f"Your Score {self.score}/{self.question_number} ")
        else:
            print("Wrong Answer")
            print(f"Your Score {self.score}/{self.question_number} ")
        


