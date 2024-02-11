from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

TURTLE_COLOR = "#F4C2C2"

class Player(Turtle):
    """
    Classe que representa a tartaruga no jogo.
    """
    def __init__(self):
        """
        Construtor da classe.

        Cria e posiciona a tartaruga.
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.color(TURTLE_COLOR)

    def move_up(self):
        """
        Move a tartaruga para frente
        """
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """
        Retorna True ou False se a posição Y for maior ou menor que a constante FINISH_LINE_Y.
        """
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        """
        Move a tartaruga para o início.
        :return:
        """
        self.goto(STARTING_POSITION)
