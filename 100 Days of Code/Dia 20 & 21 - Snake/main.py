from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Cria a tela principal do jogo e configura a altura e a largura da tela.
screen = Screen()
screen.setup(width=600, height=600)
# Desativa a atualização automática da tela.
screen.tracer(0)
# Define a cor de fundo e o titulo da janela.
screen.bgcolor("#191919")
screen.title("Snake Game")

# Cria os objetos, Snake, Food e Scoreboard.
snake = Snake()
food = Food()
score = Scoreboard()

# Ativa o controle de teclado na tela.
screen.listen()
# Vincula os métodos de movimento da Snake as setas.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Variável para controlar o loop do jogo.
game_is_on = True
# Loop do jogo.
while game_is_on:
    # Atualiza a tela e pausa por 0.1 segundos.
    screen.update()
    time.sleep(0.1)

    # Move a Snake.
    snake.move()

    # Detecta a colisão com a comida e aumenta a pontuação.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detecta colisão com as bordas da tela.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detecta colisão coma cauda.
    for segment in snake.segments[1:]:
        # Finaliza o jogo.
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

# Mantém a janela do jogo aberta.
screen.mainloop()