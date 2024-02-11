from turtle import Turtle

LEVEL_COLOR = "#E5E6E4"
LEVEL_FONT = ("Century Gothic", 15, "normal")
LEVEL_FONT_POSITIONS = (-290, 270)
LEVEL_ALIGNMENT = "left"

GAMEOVER_COLOR = "#8B0000"
GAMEOVER_FONT = ("Century Gothic", 20, "normal")
GAMEOVER_FONT_POSITION = (0, 0)
GAMEOVER_ALIGNMENT = "center"

class Scoreboard(Turtle):
    """
    Classe que representa o nivel no jogo.
    """
    def __init__(self):
        """
        Construtor da classe.

        Cria e posiciona o placar com o nível no jogo.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_FONT_POSITIONS)
        self.level = 1
        self.color(LEVEL_COLOR)
        self.update()

    def update(self):
        """
        Atualiza o placar.
        """
        self.clear()
        self.write(arg=f"Level: {self.level}", align=LEVEL_ALIGNMENT, font=LEVEL_FONT)

    def make_score(self):
        """
        Aumenta o nível.
        """
        self.level += 1
        self.update()
        
    def game_over(self):
        """
        Finaliza o jogo.
        """
        self.color(GAMEOVER_COLOR)
        self.goto(GAMEOVER_FONT_POSITION)
        self.write(arg="GAME OVER", align=GAMEOVER_ALIGNMENT, font=GAMEOVER_FONT)