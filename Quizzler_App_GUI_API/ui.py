import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizzlerUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tk.Label(text="Score: 0/0", font=("Arial", 12, "normal"), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_canvas = self.canvas.create_text(150, 125, text="question", font=FONT, width=280)

        self.true_button_image = tk.PhotoImage(file="./images/true.png")
        self.false_button_image = tk.PhotoImage(file="./images/false.png")

        self.true_button = tk.Button(image=self.true_button_image,
                                     highlightthickness=0,
                                     command=self.true_button_func)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(image=self.false_button_image,
                                      highlightthickness=0,
                                      command=self.false_button_func)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_canvas, text=ques_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_canvas,
                                   text="You have reached to the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_func(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_func(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

    # def original_bg(self):
    #     self.canvas.config(bg="white")
    #     self
