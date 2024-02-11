from turtle import Turtle

SCORE_COLOR = "#FFE4E1"
GAMEOVER_COLOR = "#8B0000"

ALIGNMENT = "center"
SCORE_FONT = ("Century Gothic", 45, "normal")

class Scoreboard(Turtle):
    """
    "Classe que representa o placar do jogo de Pong. Estende a classe Turtle da biblioteca turtle.
    """
    def __init__(self, position_x):
        """
        Construtor da classe.

        Chama o construtor da superclasse e define a cor e a posição do placar.
        :param position_x: Posição X do placar.
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color(SCORE_COLOR)
        self.goto(x=position_x, y=200)
        self.update()

    def update(self):
        """
        Atualiza a pontuação.
        """
        self.clear()
        self.write(arg=f"{str(self.score).zfill(2)}", align=ALIGNMENT, font=SCORE_FONT)

    def make_score(self):
        """
        Aumenta a pontuação em 1.
        """
        self.score += 1
        self.update()