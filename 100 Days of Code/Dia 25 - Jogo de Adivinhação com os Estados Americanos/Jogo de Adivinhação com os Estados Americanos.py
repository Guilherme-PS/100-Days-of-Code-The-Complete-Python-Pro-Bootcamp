import turtle
import pandas as pd

# Imagem de fundo.
BACKGROUND = "blank_states_img.gif"

# Configurações usadas para escrever o nome dos estados.
NAME_FONT = ("Century Gothic", 7, "normal")
NAME_COLOR = "#000000"
NAME_ALIGNMENT = "center"

# Lê o arquivo .CSV com os nomes dos estados e suas coordenadas.
df = pd.read_csv("50_states.csv")

# Cria e configura a janela do jogo.
screen = turtle.Screen()
screen.title("U.S State Game")

# Adiciona a imagem no fundo da janela.
screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)

# Lista para armazenar os estados adivinhados.
guessed_states = list()

# Loop para continuar o jogo até que todos os estados sejam adivinhados.
while len(guessed_states) < 50:
    # Solicita ao usuário que tente adivinhar um estado.
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 Estados Corretos",
                                  prompt="Qual o nome do estado?").title()

    # Verifica se o usuário digitou "exit" para sair do jogo.
    if user_guess == "Exit":
        # Cria uma lista com os estados não adivinhados.
        states_to_learn = [state for state in df["states"].to_list() if state not in guessed_states]
        # Cria um arquivo .CSV com os estados não adivinhados.
        states_to_learn = pd.DataFrame(states_to_learn)
        states_to_learn.to_csv("Staves_to_Learn.csv")
        break

    # Verifica se o usuário adivinhou um estado correto e que ainda não foi adivinhado.
    if user_guess not in guessed_states and user_guess in df["state"].to_list():
        # Inicializa o turtle para escrever o nome do estado.
        t = turtle.Turtle()
        t.color(NAME_COLOR)
        t.penup()
        # Vai para as coordenadas X e Y do estado adivinhado.
        t.goto(x=int(df[df.state == user_guess].x), y=int(df[df.state == user_guess].y))
        t.write(arg=user_guess, align=NAME_ALIGNMENT, font=NAME_FONT)
        t.hideturtle()

        # Adiciona o estado adivinhado na lista.
        guessed_states.append(user_guess)