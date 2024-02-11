import pandas as pd

# Lendo o arquivo .CSV.
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Criando um dicionário onde cada chave é uma letra e cada valor é o código fonético NATO correspondente.
nato_alphabet = {row["letter"]: row["code"] for index, row in df.iterrows()}

# Loop infinito.
while True:
    # Solicita que o usuário digite uma palavra.
    user_word = input("Digite uma palavra: ").upper()

    # Tenta criar uma lista com os valores correspondentes as letras do alfabeto.
    try:
        new_word = [nato_alphabet[letter] for letter in user_word]
    # Tratamento de exceção para letras não presentes no dicionário.
    except KeyError:
        print("Por favor, digite apenas letras.")
    # Se não ocorrer uma exceção, imprime a lista e encerra o loop.
    else:
        print(new_word)
        break