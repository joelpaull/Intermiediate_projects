class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q{int(self.question_number) +1}: {current_question.text} True/False?\n").capitalize()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)


    def still_has_questions(self):
        if int(len(self.question_list)) == self.question_number:
            return False
        return True

    def check_answer(self, user_answer, current_answer):
        if str(user_answer) == str(current_answer):
            self.correct += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong")
        print(f'{self.correct}/{self.question_number}')