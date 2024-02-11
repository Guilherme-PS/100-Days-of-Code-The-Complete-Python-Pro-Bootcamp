from turtle import Turtle

SCORE_COLOR = "#E5E6E4"
GAMEOVER_COLOR = "#8B0000"

ALIGNMENT = "center"
SCORE_FONT = ("Century Gothic", 15, "normal")

GAMEOVER_FONT = ("Century Gothic", 18, "normal")

class Scoreboard(Turtle):
    """Inicializa a pontuação e exibe a pontuação atual"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)

        self.update()

    def update(self):
        """
        Atualiza a exibição da pontuação.
        """
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        """
        Aumenta a pontuação em 1 e atualiza a exibição da pontuação
        """
        self.score += 1
        self.update()

    def reset(self):
        """
        Verifica se a pontuação atual é maior que a variável "high_score".
        """
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()