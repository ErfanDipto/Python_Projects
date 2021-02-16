from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
# que_end = False
for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))


# TODO 1: asking the questions

question_pass = QuizBrain(question_bank)

while question_pass.still_has_question():
    question_pass.next_question()

# TODO 2: checking if the answer was correct
#     question_pass.check_answer()
# TODO 3: checking if we are end of the quiz

# if question_pass.still_has_question():
#     ques_end = True
# else:
#     ques_end = False
# q1 = Question("yo", True)
# # q1.text = "Yo"
# # q1.answer = True
# print(q1.text)
# print(q1.answer)
# print(question_data[4]["text"])
# question_bank.append(Question(question_data[0]["text"], question_data[0]["answer"]))
# print(question_bank[0].text)
