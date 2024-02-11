import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#5A2050"
CORRECT_BALLON_COLOR = "#4BAE4F"
WRONG_BALLON_COLOR = "#CB2323"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Atributo que armazena a lógica do quiz.
        self.quiz = quiz_brain

        # Criação da janela principal do aplicativo.
        self.root = tk.Tk()
        self.root.title("Quiz")
        self.root.geometry("350x420")
        self.root.resizable(width=False, height=False)

        # Carregamento das imagens usadas na interface.
        self.ballon_image = tk.PhotoImage(file="images/Ballon.png")
        self.correct_ballon = tk.PhotoImage(file="images/Correct_Ballon.png")
        self.wrong_ballon = tk.PhotoImage(file="images/Wrong_Ballon.png")

        self.correct_button_image = tk.PhotoImage(file="images/Correct_Button.png")
        self.wrong_button_image = tk.PhotoImage(file="images/Wrong_Button.png")

        # Cria o canvas para desenhar a interface.
        self.canvas = tk.Canvas(width=350, height=450, background=THEME_COLOR)

        # Adiciona as imagens e elementos de texto ao canvas.
        self.ballon = self.canvas.create_image(175, 172, image=self.ballon_image)
        self.text = self.canvas.create_text(175, 145, width=225, text="Question", font=("Century Gothic", 11, "normal"))
        self.score = self.canvas.create_text(175, 37, text=f"Score: {self.quiz.score}",
                                             font=("Century Gothic", 12, "normal"), fill="#FFFFFF")
        self.canvas.pack()

        # Cria e posiciona os botões de resposta "correta" e "incorreta".
        self.correct_button = tk.Button(image=self.correct_button_image, relief="flat", background=THEME_COLOR,
                                        activebackground=THEME_COLOR, command=self.right)
        self.correct_button.place(x=71, y=300)

        self.wrong_button = tk.Button(image=self.wrong_button_image, relief="flat", background=THEME_COLOR,
                                      activebackground=THEME_COLOR, command=self.wrong)
        self.wrong_button.place(x=71, y=350)

        # Gera a primeira pergunta.
        self.gen_question()

        # Inicia o loop de eventos.
        self.root.mainloop()

    def gen_question(self):
        # Volta a exibir a imagem do balão de fala.
        self.canvas.itemconfig(self.ballon, image=self.ballon_image)

        # Se ainda há perguntas no quiz, gera a próxima pergunta e atualiza o score.
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.score, text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        # Caso contrário, exibe uma mensagem de fim de quiz e desabilita os botões.
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        # Chama o método de verificação de resposta do QuizBrain passando "True" como resposta.
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        # Chama o método de verificação de resposta do QuizBrain passando "False" como resposta.
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        # Se a resposta foi correta, exibe a imagem de um balão de fala verde.
        if is_right:
            self.canvas.itemconfig(self.ballon, image=self.correct_ballon)
            # Se a imagem foi incorreta, exibe a imagem de um balão de fala vermelho.
        else:
            self.canvas.itemconfig(self.ballon, image=self.wrong_ballon)

        # Aguarda 1 segundo e gera a próxima pergunta.
        self.root.after(1000, self.gen_question)
