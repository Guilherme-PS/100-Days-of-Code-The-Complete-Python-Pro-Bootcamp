from random import choice
from Data import data
from Art import vs

# Variáveis para armazenar os valores escolhidos aleatóriamente.
data_A = data_B = ""
# Pontuação do jogador.
score = 0

# Boas vindas ao usuário.
print("Bem-vindo ao Jogo: Higher Lower Game!\n")

# Faz o jogo ser repetitivo
while data_A == data_B:
    # Escolhe um valor aleatório a partir dos dados do jogo.
    data_A, data_B = choice(data), choice(data)

    # Verifica se os dados são diferentes.
    if data_A != data_B:
        # Imprime os dados a serem comparados e a arte "vs" em ASCII.
        print(f"Dado A: {data_A['name']}, {data_A['description']}, mora em: {data_A['country']}")
        print(vs)
        print(f"Dado B: {data_B['name']}, {data_B['description']}, mora em: {data_B['country']}")

        # Solicita ao usuário que escolha entre A ou B
        result = input("\nQuem tem mais seguidores? Digite [A] ou [B]: ").upper()

        # Verifica qual dos dados gerados é maior e compara com a entrada do usuário.
        if (data_A["follower_count"] > data_B["follower_count"]) and result == "A":
            score += 1
        elif (data_B["follower_count"] > data_A["follower_count"]) and result == "B":
            score += 1
        # Para o jogo caso o usuário erre.
        else:
            print(f"Você Errou. Pontuação Final: {score}")
            exit()

        # Imprime caso o usuário acerte.
        print(f">>> Você Acertou! Pontuação Atual: {score}\n")

    # Zera o valor dos dados.
    data_A = data_B = ""