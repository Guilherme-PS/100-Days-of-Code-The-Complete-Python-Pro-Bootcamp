# Importa o módulo turtle e random.
import turtle
import random
# Importa as cores.
from color_data import colors

def change_side(line_number):
    """
    Altera a linha em que a tartaruga está.
    :param line_number: O número em que a tartaruga está.
    """
    tim.setheading(90)
    tim.forward(50)

    if line_number % 2 == 0:
        tim.left(90)
    else:
        tim.right(90)

    tim.forward(50)


# Configura o modo de cor da tartaruga
turtle.colormode(255)

# Cria uma instãncia da tartaruga
tim = turtle.Turtle()
# Oculta o cursor da tartaruga e define a velocidade como máxima.
tim.hideturtle()
tim.speed("fastest")

# Levanta a caneta e move a tartaruga para a posição inicial.
tim.penup()
tim.goto(x=-529, y=-222)
tim.forward(300)
tim.setheading(0)

# Loop para desenhar os pontos.
for line in range(10):
    for _ in range(10):
        # Desenha um ponto com uma cor aleatória.
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    # Altera o lado.
    change_side(line)

# Cria a janela e aguarda o clique do usuário para sair.
screen = turtle.Screen()
screen.exitonclick()