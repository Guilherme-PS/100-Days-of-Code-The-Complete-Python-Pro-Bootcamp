from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Posições iniciais para as raquetes e placares.
STARTING_POSITIONS = (-350, 350, )
SCORE_POSITIONS = (-100, 100)

# Cria e configura a janela.
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("#191919")
screen.setup(width=800, height=600)
# Desativa a atualização automática da tela.
screen.tracer(0)

# Cria a raquete e o placar da direta.
right_paddle = Paddle(STARTING_POSITIONS[1])
right_score = Scoreboard(SCORE_POSITIONS[1])
# Cria a raquere e o placar da esquerda.
left_paddle = Paddle(STARTING_POSITIONS[0])
left_score = Scoreboard(SCORE_POSITIONS[0])

# Cria a bola
ball = Ball()

# Habilita a captura de eventos do teclado.
screen.listen()
# Mapeia as setas do teclado para mover a raquete da direita para cima e para baixo.
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
# Mapeia as teclas "w" e "s" para mover a raquete esquerda para cima e para baixo.
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

# Variável para controlar o loop do jogo.
game_is_on = True
# Loop principal do jogo.
while game_is_on:
    # Pausa o jogo por 0.05 segundos.
    time.sleep(0.05)
    # Atualiza a tela.
    screen.update()
    # Move a bola.
    ball.move()

    # Verifica a colisão da bola com as bordas da tela.
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.vertical_bounce()

    # Verifica a colisão da bola com as raquetes.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.horizontal_bounce()

    # Verifica pontuação e reposiciona a bolinha para o centro.
    if ball.xcor() > 380:
        ball.reset_position()
        left_score.make_score()
    elif ball.xcor() < -380:
        ball.reset_position()
        right_score.make_score()

# Fecha a janela do jogo quando o usuário clica nela.
screen.exitonclick()