from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.window.title("QUIZZER")
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()
        true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_image, highlightthickness=0, command=self.right)
        self.right_button.grid(column=0, row=2)
        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label = Label(text=f"score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end!!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        user_answer = "true"
        self.give_feedback(self.quiz.check_answer(user_answer))

    def false(self):
        user_answer = "false"
        self.give_feedback(self.quiz.check_answer(user_answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
