# Importa o módulo random e turtle.
import turtle
import random

def create_turtles(color):
    """
    Cria uma tartaruga com a cor especificada.
    :param color: Cor da tartaruga.
    :return: Tartaruga criada.
    """
    tim = turtle.Turtle(shape="turtle")
    tim.color(color)
    tim.penup()

    return tim

def bet(turtle_names):
    """
    Solicita ao usuário que escolha uma das tartarugas presentes na lista para apostar.
    :param turtle_names: Lista de tartarugas.
    :return: Nome da tartaruga escolhida pelo usuário.
    """
    while True:
        user_bet = screen.textinput(title="Faça a Sua Aposta",
                                    prompt="Qual Tartaruga vai Ganhar a Corrida? Digite a Cor: ").title()

        if user_bet in turtle_names:
            return user_bet
        else:
            print("Opção Inválida!")


# Inicializa a tela do turtle e define a dimensão da janela.
screen = turtle.Screen()
screen.setup(width=500, height=400)

# Define o nome e as cores das tartarugas.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_names = ["Vermelha", "Laranja", "Amarela", "Verde", "Azul", "Roxa"]
# Cria um dicionário para armazenar todas as tartarugas.
all_turtles = dict()
# Cria as tartarugas com as cores especificadas e as adiciona no dicionário.
for num in range(6):
    all_turtles[color_names[num]] = create_turtles(colors[num])
# Posiciona as tartarugas na partida.
position = 60
for turtle in all_turtles.values():
    turtle.goto(x=-230, y=position)

    position -= 25
# Solicita ao usuário que ele escolha uma tartaruga para apostar.
user_choice = bet(all_turtles.keys())

# Loop principal da corrida
is_race_on = True
while is_race_on:
    for turtle_name, turtle in all_turtles.items():
        # Tartaruga anda para frente um número aleatório de pixels.
        turtle.forward(random.randint(0, 10))
        # Verifica se a tartaruga atingiu o ponto de chegada.
        if turtle.xcor() > 230:
            # Exibe o nome da tartaruga vencedora.
            print(f">>> A Tartaruga {turtle_name} Ganhou.")
            # Verifica se a tartaruga escolhida pelo usuário é a vencedora.
            if user_choice == turtle_name:
                print("Você Ganhou!")
            else:
                print("Você Perdeu.")
            # Interrompe o loop.
            is_race_on = False

# Fecha a janela se o usuário clicar.
screen.exitonclick()