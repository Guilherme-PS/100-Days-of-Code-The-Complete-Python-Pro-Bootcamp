class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_input = input(f">>> Q.{self.question_number+1}: {self.question_list[self.question_number].card_word} "
                           f"[True/False]?\nR.: ")
        self.check_answer(user_input)

    def check_answer(self, answer):
        if answer.title() == self.question_list[self.question_number].answer:
            self.score += 1
            print(f"\nVocê acertou!")
        else:
            print(f"\nVocê errou.")
            print(f"A resposta correta era: {self.question_list[self.question_number].answer}.")

        self.question_number += 1
        print(f"Pontuação Atual: {self.score}/{self.question_number}\n")
