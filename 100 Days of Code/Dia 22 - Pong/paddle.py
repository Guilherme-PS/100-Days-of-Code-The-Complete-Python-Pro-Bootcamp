from turtle import Turtle

SHAPE_LEN = 1
SHAPE_WID = 5

PADDLE_COLOR = "#E5E6E4"

class Paddle(Turtle):
    """
    Classe que representa as raquetes do jogo de Pong. Estende a classe Turtle da biblioteca turtle.
    """
    def __init__(self, position_x):
        """
        Construtor da classe. Chama o construtor da superclasse e define a forma, cor e a posição da raquete.
        :param position_x: Posição X da raquete.
        """
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.penup()
        self.goto(x=position_x, y=0)
        self.turtlesize(stretch_len=SHAPE_LEN, stretch_wid=SHAPE_WID)

    def move_up(self):
        """
        Move a raquete 20 pixels para cima.
        """
        self.goto(self.xcor(), self.ycor() + 30)

    def move_down(self):
        """
        Move a raquete 20 pixels para baixo.
        """
        self.goto(self.xcor(), self.ycor() - 30)