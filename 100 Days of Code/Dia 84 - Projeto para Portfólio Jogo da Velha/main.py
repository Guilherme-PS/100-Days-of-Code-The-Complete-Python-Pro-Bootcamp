from random import randint

# Menu Inicial
def menu():
    print(f"{'─=─' * 15}\n\t\t\t\t\033[1mJOGO DA VELHA\033[0m\n{'─=─' * 15}")
    print("Escolha uma Opção:\n\t[1] : Iniciar\n\t[2] : Sair")

    while True:
        choice = str(input(">>> "))

        if choice == "1":
            return True
        elif choice == "2":
            print("Saindo...")

            return False
        else:
            print("Opção Inválida!")


# Escolher X ou O
def player():
    print("Escolha sua Marcação:\n\t[1] : X\n\t[2] : O")

    mark = str(input(">>> "))

    if mark == "1":
        return {"player_1": "X", "player_2": "O"}

    elif mark == "2":
        return {"player_1": "O", "player_2": "X"}


# 2. Montar tabuleiro
def gen_table():
    data = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    return data

def print_table(game_table):
    print(f"  {game_table[0][0]}  │  {game_table[0][1]}  │  {game_table[0][2]}  ")
    print("─────┼─────┼─────")
    print(f"  {game_table[1][0]}  │  {game_table[1][1]}  │  {game_table[1][2]}  ")
    print("─────┼─────┼─────")
    print(f"  {game_table[2][0]}  │  {game_table[2][1]}  │  {game_table[2][2]}  ")


# Preenche o tabuleiro com os inputs do jogador
def player_input(game_table, player_mark):
    while True:
        pos = tuple(input("Escolha uma Posição: [Linha, Coluna]\n>>> ").replace(" ", "").split(","))

        try:
            if game_table[int(pos[0])][int(pos[1])] == " ":

                game_table[int(pos[0])][int(pos[1])] = player_mark
                break
            else:
                print("\nPosição já Preenchida!")

        except IndexError:
            print("\nPosição Inválida!")

# Preenche o tabuleiro com os inputs da maquina gerados aleatóriamente
def machine_input(game_table, machine_mark):
    while " " in game_table[0] or " " in game_table[1] or " " in game_table[2]:
        pos = randint(0, 2), randint(0, 2)

        if game_table[int(pos[0])][int(pos[1])] == " ":
            game_table[int(pos[0])][int(pos[1])] = machine_mark

            break


# 4. Verificar a vitória
def verify_victory(game_table, mark):
    if game_table[0] == [mark, mark, mark] or game_table[1] == [mark, mark, mark] or game_table[2] == [mark, mark, mark]:
        return True

    elif [game_table[0][0], game_table[1][0], game_table[2][0]] == [mark, mark, mark]:
        return True
    elif [game_table[0][1], game_table[1][1], game_table[2][1]] == [mark, mark, mark]:
        return True
    elif [game_table[0][2], game_table[1][2], game_table[2][2]] == [mark, mark, mark]:
        return True

    elif [game_table[0][0], game_table[1][1], game_table[2][2]] == [mark, mark, mark]:
        return True
    elif [game_table[0][2], game_table[1][1], game_table[2][0]] == [mark, mark, mark]:
        return True

    else:
         return False

# Verifica empate
def verify_draw(game_table):
    if " " not in game_table[0] and " " not in game_table[1] and " " not in game_table[2]:
        return True

    else:
        return False


# Loop principal
while menu():
    # Define as marcações para o jogador e a maquina
    players = player()

    player_mark = players["player_1"]
    machine_mark = players["player_2"]

    # Cria a tabela
    table = gen_table()

    # Loop para o jogo
    while True:
        # Imprime a tabela
        print_table(table)

        # Verifica vitória e empate
        if verify_victory(table, player_mark):
            print("O Jogador ganhou!")

            break

        elif verify_victory(table, machine_mark):
            print("A máquina ganhou!")

            break

        elif verify_draw(table):
            print("Empate!")

            break

        else:
            # Jogadas do jogador e da máquina
            player_input(table, player_mark)
            machine_input(table, machine_mark)
