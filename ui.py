from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.is_right = None
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(fg="white",text="Score: 0", bg=THEME_COLOR )
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas()
        self.canvas.config(bg="white", height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question Text here",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Arial", 20, "italic"))

        self.right_button = Button()
        right_image = PhotoImage(file="images/true.png")
        self.right_button.config(image=right_image, command=self.correct, highlightthickness=0 )
        self.right_button.grid(row=2, column=0)
        self.left_button = Button()
        left_image = PhotoImage(file="images/false.png")
        self.left_button.config(image=left_image, command=self.incorrect, highlightthickness=0)
        self.left_button.grid(row=2, column=1)
        self.get_next_question()



        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.update_score()
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of Quiz")

    def correct(self):
        self.is_right = self.quiz.check_answer("true")
        self.give_feedback()
    def incorrect(self):
        self.is_right = self.quiz.check_answer("false")
        self.give_feedback()

    def update_score(self):
        self.score_label.config(text=f"Score {self.quiz.score} / {self.quiz.question_number - 1}")

    def give_feedback(self):
        if self.is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.screen.after(1000, func=self.get_next_question)




