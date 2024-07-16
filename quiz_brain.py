class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """ get the question from Question class. """
        current_question = self.question_list[self.question_number]  # question_bank[0] -> Question(q_text, q_answer).
        self.question_number += 1 # increment before printing
        guess = input(f"Q.{self.question_number} {current_question.text} (True or False):  ")
        self.check_answer(guess, current_question.answer)  # used 'self' word to execute method inside its class.

    def check_answer(self, guess, correct_answer):
        if correct_answer.lower() == guess.lower():  # used lower method on both to make sure it'll be the same.
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n" * 1)  # separator

    def still_has_question(self):
        """return True if question number is less than length of question list."""
        return self.question_number < len(self.question_list)  # return True or False. question number starts from zero



