from tkinter import *
from quiz_brain import QuizBrain
from time import time

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz:QuizBrain):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.question_text=self.canvas.create_text(150,125,fill=THEME_COLOR,width=280,font=("Arial",20,"italic"))

        self.check_image=PhotoImage(file="images/true.png")
        self.wrong_image=PhotoImage(file="images/false.png")

        self.check_button=Button(image=self.check_image,highlightthickness=0,command=self.answer_check_true)
        self.check_button.grid(row=2,column=0)

        self.wrong_button=Button(image=self.wrong_image,highlightthickness=0,command=self.answer_check_false)
        self.wrong_button.grid(row=2,column=1)

        self.label=Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",15,"italic"))
        self.label.grid(row=0,column=1)
        self.show_question()


        self.window.mainloop()

    def show_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label.config(text=f"Score: {self.quiz.score}")
            curr_question=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=curr_question)
        elif self.quiz.question_number==10:
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text="You've reached the final question of the game.")
            self.canvas.config(bg="white")
            self.wrong_button.config(state="disabled") #this is how you disable the function calling after pressing that button,it disables command attribute
            self.check_button.config(state="disabled")

    def answer_check_true(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_check_false(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.show_question)

