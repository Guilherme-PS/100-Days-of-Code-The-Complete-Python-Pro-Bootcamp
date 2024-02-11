from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Criando uma lista vazia para armazenar as perguntas.
question_bank = []
# Iterando sobre os dados das perguntas.
for question in question_data:
    # Obtendo o texto da pergunta e a resposta correta.
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Criando uma nova instância da classe Question.
    new_question = Question(question_text, question_answer)
    # Adicionando a pergunta a lista de perguntas.
    question_bank.append(new_question)

# Criando uma instância da classe QuizBain e passando a lista de perguntas.
quiz = QuizBrain(question_bank)
# Criando uma instância da classe QuizInterface e passando a instância QuizBrauin.
quiz_ui = QuizInterface(quiz)