# Importando o módulo random.
import random

# Strings que representam pedra, papel e tesoura em ASCII.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lista com as strings ASCII.
options = [rock, paper, scissors]

# Solicita ao usuário uma das opções do jogo, digitando um número de 0 a 2.
user_input = int(input("O que você escolhe? [0] Pedra, [1] Papel ou [2] para Tesoura. "))

# Utiliza função randint do módulo random para gerar um número aleatório.
machine_input = random.randint(0, len(options)-1)

# Verifica se a entrada do usuário está entre 0 e 2.
if user_input in [0, 1, 2]:
    # Imprime as strings ASCII.
    print(f"{options[user_input]}\nComputador:\n{options[machine_input]}")

    # Verifica o resultado do jogo comparando as escolhas do usuário com a do computador.
    if user_input == 0 and machine_input == 2:
        print("Você Ganhou!")
    elif user_input == 1 and machine_input == 0:
        print("Você Ganhou!")
    elif user_input == 2 and machine_input == 1:
        print("Você Ganhou!")
    elif user_input == machine_input:
        print("Empate!")
    else:
        print("Você Perdeu.")

# Finaliza o jogo caso o usuário digite um número fora do intervalo 0 e 2.
else:
    print("Número inválido!\nVocê Perdeu.")