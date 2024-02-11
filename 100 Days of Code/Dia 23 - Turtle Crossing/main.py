from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Cria e configura a tela.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#252525")
screen.title("Turtle Crossing")
# Desativa a atualização automática da tela.
screen.tracer(0)

# Cria o jogador, os carros e o placar.
player = Player()
car_manager = CarManager()
score = Scoreboard()

# Habilita a captura de eventos do teclado.
screen.listen()
# Mapeia a seta para cima para mover a tartaruga para frente.
screen.onkey(fun=player.move_up, key="Up")

# Variável para controlar o loop do jogo.
game_is_on = True
# Loop principal do jogo.
while game_is_on:
    # Pausa o jogo por 0.1 segundos e atualiza a tela.
    time.sleep(0.1)
    screen.update()

    # Gera novos carros.
    car_manager.gen_cars()
    # Move os carros gerados para frente.
    car_manager.move_cars()

    # Verifica a colisão com o carro.
    for car in car_manager.cars:
        if car.distance(player) < 25:
            score.game_over()
            game_is_on = False

    # Verifica se o player chegou ao outro lado.
    if player.is_at_finish_line():
        score.make_score()
        player.reset_position()
        car_manager.increase_difficulty()

# Fecha a janela do jogo quando o usuário clica nela.
screen.exitonclick()