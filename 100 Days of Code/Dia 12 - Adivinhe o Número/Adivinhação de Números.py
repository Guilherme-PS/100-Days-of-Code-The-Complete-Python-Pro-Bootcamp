# Importa a função randint do módulo random.
from random import randint
# Importa a função sleep do módulo time.
from time import sleep

# Boas vindas ao usuário.
print("Bem-vindo ao Jogo de Adivinhação de Números!\n")
print("Estou Pensando em um Número entre 1 e 100...\n")

# Pausa o programa por 1 segundo.
sleep(1)
# Gera um número aleatório entre 1 e 100.
number = randint(1, 100)


def result_check(user_input):
    """
    Verifica se o número adivinhado pelo usuário é maior ou menor do que o número gerado pelo programa.
    :param user_input: Número adivinhado pelo usuário.
    :return: None
    """
    if user_input > number:
        print("\n>>> Muito Alto.")
    elif user_input < number:
        print("\n>>> Muito Baixo.")


# Solicita ao usuário que escolha uma dificuldade.
difficulty = input("Escolha uma dificuldade. Digite [Fácil] ou [Difícil]: ").title()
# Define o número de tentativas baseado na dificuldade que o usuário escolheu.
if difficulty == "Fácil" or difficulty == "Facil":
    attempts = 10
elif difficulty == "Difícil" or difficulty == "Dificil":
    attempts = 5
else:
    print("Dificuldade não encontrada. Dificuldade definida como: Fácil\n")
    attempts = 10

# Mantém o jogo em loop, baseado na quantidade de tentativas que o usuário possui.
while attempts != 0:
    # Retorna a quantidade de tentativas restantes.
    print(f"Você tem {attempts} para tentar adivinhar o número.")
    # Solicita ao usuário que tente adivinhar o número.
    user_guess = int(input("Tente adivinhar o número: "))

    # Verifica se o número solicitado pelo usuário é igual ao número gerado.
    if user_guess == number:
        print(f"\nVocê Ganhou! O número é: {number}.")
        break

    # Verifica se o número solicitado pelo usuário está entre 1 e 100 e verifica se ele é maior ou menor.
    if 1 <= user_guess <= 100:
        result_check(user_guess)
        attempts -= 1
    else:
        print("Digite números entre 1 e 100.")
# Retorna uma mensagem caso o número de tentativas chegue a 0.
else:
    print(f"\nVocê Perdeu! O número era: {number}.")