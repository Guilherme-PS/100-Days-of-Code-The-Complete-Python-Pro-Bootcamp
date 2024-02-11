# Importa as artes do jogo.
from Art import welcome_art, stages
# Importa as palavras para o jogo.
from Word import words
# Importa o módulo random.
import random

# Armazena as palavras possíveis para o jogo.
word_list = word

# Escolhe aleatóriamente uma palavra da lista.
word = random.choice(word_list)
# Converte a variável "word" em uma lista.
chosen_word = list(word)
# Cria uma lista com o mesmo tamanho da lista "chosen_word", todos os elementos dessa lista são "_".
display = ["_"] * len(chosen_word)
# Armazena a quantidade de vidas do jogador.
lives = 6

print(welcome_art)
print("Para Ganhar, Adivinhe a Palavra.\n")

# Loop infinito para o jogador tentar adivinhar a palavra.
while True:
    # Imprime o desenho atual da forca.
    print(stages[lives])

    # Imprime as letras que o usuário acertou.
    for line in display:
        print(line, end=" ")

    # Imprime a quantidade de vidas que o jogador possui.
    print(f"\n\nVidas: {lives}")
    # Solicita o usuário que tente adivinhar uma letra.
    user_input = input(">>> Adivinhe uma Letra: ").lower()

    # Verifica se a entrada do usuário está na palavra.
    if user_input in chosen_word:
        for letter in chosen_word:
            # Substitui a letra
            if letter == user_input:
                display[chosen_word.index(letter)] = user_input
                # Insere um X na lista "chose_word" para evitar que a letra seja contada novamente.
                chosen_word[chosen_word.index(letter)] = "X"

    # Retorna uma mensagem caso o jogador tente digitar uma letra que já tenha sido adivinhada.
    elif user_input in display:
        print(f"Você já adivinhou essa letra: \033[1m{user_input}\033[0m")

    # Retorna uma mensagem caso o jogador erre e remove uma vida
    else:
        print(f"Você tentou a letra: '{user_input}', ela não está na palavra.\nVocê perdeu uma vida.")
        lives += -1

    # Se todos os caracteres da lista "display" forem diferentes de "_", o jogador vence e o loop é interrompido.
    if "_" not in display:
        print(f"\n{word}\nVocê Ganhou!")
        break
    # Se a variável "lives" for igual a 0, o jogador perde o jogo.
    elif lives == 0:
        print(f"\n{word}\nVocê Perdeu.")
        break