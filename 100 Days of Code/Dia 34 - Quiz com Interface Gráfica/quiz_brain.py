import html

class QuizBrain:
    # Método construtor da classe.
    def __init__(self, q_list):
        # Atributo que armazena o número da pergunta atual.
        self.question_number = 0
        # Atributo que armazena a pontuação do usuário.
        self.score = 0
        # Atributo que armazena a lista de perguntas.
        self.question_list = q_list
        # Atributo que armazena a pergunta atual.
        self.current_question = None

    # Método que verifica se ainda há perguntas a serem respondidas.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Método que retorna a próxima pergunta e incrementa o número da pergunta atual.
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    # Método que verifica se a resposta do usuário está correta atualiza a pontuação.
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False