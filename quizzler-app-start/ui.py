THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(height=300,width=300,bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width = 280,
                                                     text="Some Type Questions",
                                                     font=("Arial",20," bold italic"))
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.true_button.grid(row = 2, column =  0)
        self.false_button.grid(row = 2, column = 1)
        self.get_question()
        self.window.mainloop()
    def get_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score : {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=question)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_question)
