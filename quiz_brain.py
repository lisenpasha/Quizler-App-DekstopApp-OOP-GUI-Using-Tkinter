import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None #we declare it as an attribute so we can use it anywhere inside class

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number] #select the question object depending on question number we currently are
        self.question_number += 1
        curr_question=html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {curr_question} "
        # user_answer = input(f"Q.{self.question_number}: {curr_question} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
