from question_model import Question


# Previous versions of this project used to get data 
# from the data moule created by me. But now
# it gethers data from opentb API

# from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizzlerUI


parameter = {"amount": 10,
             "type": "boolean"}

response = requests.get("https://opentdb.com/api.php?", params=parameter)
response.raise_for_status()
question_data = response.json()['results']
print(question_data)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizzlerUI(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
