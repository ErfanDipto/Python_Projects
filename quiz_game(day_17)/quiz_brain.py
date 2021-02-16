# from main import question_bank

class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return not self.question_number == len(self.question_list)

    def next_question(self):
        que_in = input(f'Q {self.question_number + 1}.{self.question_list[self.question_number].text} True/False: ')
        self.check_answer(que_in, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, que_in, ques_ans):
        self.user_input = que_in
        self.ans = ques_ans
        if self.user_input.lower() == self.ans.lower():
            self.score += 1
            print("Correct answer!!")
            print(f"Score: {self.score}/{self.question_number+1}")
        elif (self.user_input.lower() == 'false' and self.ans.lower() == 'true') or \
                (self.user_input.lower() == 'true' and self.ans.lower() == 'false'):
            print("Wrong answer")
            print(f"Score: {self.score}/{self.question_number+1}")
        else:
            print("Invalid input. Try again")
            self.question_number -= 1
