# Importando bibliotecas
from unidecode import unidecode

# Dicionário com a conversão das letras e números
morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
         "E": ".", "F": "..-.", "G": "--.", "H": "....",
         "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
         "M": "--", "N": "-.", "O": "---", "P": ".--.",
         "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
         "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
         "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
         "3": "...--", "4": "....-", "5": ".....", "6": "-....",
         "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

# Menu inicial
print("+" + "──" * 23 + "+")
print("│   + Conversor de Texto para Código Morse +   │")
print("+" + "──" * 23 + "+")
print("│     \033[1m1\033[0m. Converter Texto" + " " * 23 + "│")
print("│     \033[1m2\033[0m. Sair" + " " * 34 + "│")
print("+" + "──" * 23 + "+")

# Escolher opção
option = input("\n Escolha uma Opção:\n \033[1m>>>\033[0m ")

# Loop para verificar se a opção escolhida está correta
while option not in ("1", "2"):
    print("\n Opção Inválida")
    option = input(" Escolha uma Opção:\n \033[1m>>>\033[0m ")

# Loop principal
while option == "1":
    # Digitar o texto e removendo acentuação com a biblioteca unidecode
    text = unidecode(input("\n Digite um Texto:\n \033[1m>>>\033[0m "))

    # Lista vazia
    translated_text = list()

    # Loop para converter o texto e armazenar as letras convertidas na lista
    for l_position in range(len(text)):
        translated_text.append(morse[text[l_position].upper()])

    # Imprime o texto original
    print(f"\n Texto Original:\n  {text}")

    # Imprime o texto convertido
    print(f"\n Texto em Código Morse:\n  {' '.join(translated_text)}")

    # Recomeça o programa
    reset = input("Deseja Converter outro Texto? [S/N] ").upper()

    # Interrompe o programa
    if reset == "N":
        break



