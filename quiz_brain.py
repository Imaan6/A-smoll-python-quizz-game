class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_questions(self):
        if self.question_number < 12:
            return (True)
        else:
            return (False)
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{question.text} (True/False):")
        self.check_answer(user_answer, question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Answer is correct")
            self.score += 1
        else:
            print("Answer is incorrect")
        print(f"The correct answer is :{correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")