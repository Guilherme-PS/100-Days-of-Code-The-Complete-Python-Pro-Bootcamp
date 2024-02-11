from turtle import Turtle

BALL_COLOR = "#800000"

class Ball(Turtle):
    """
    Classe que representa a bola do jogo Pong.

    Estende a classe Turtle da biblioteca turtle e herda todos os seus métodos e atributos.
    """
    def __init__(self):
        """
        Construtor da classe.

        Define a forma e a cor da bola como um círculo vermelho e inicializa os atributos x_move e y_move.
        """
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()

        self.x_move = 10
        self.y_move = 10

    def move(self):
        """
        Move a bola na tela usando os valores de x_move e y_move.
        """
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def vertical_bounce(self):
        """
        Inverte a velocidade da bola no eixo y.
        """
        self.y_move *= -1

    def horizontal_bounce(self):
        """
        Inverte a velocidade da bola no eixo x.
        """
        self.x_move *= -1

    def reset_position(self):
        """
        Reposiciona a bola no centro da tela e inverte o movimento inicial da bola.
        """
        self.home()
        self.horizontal_bounce()