# Importando o módulo random.
import random

# Lista com letras minúsculas e maiúsculas.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Lista de números 0 - 9.
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lista de símbolos
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Lista vazia para armazenar a senha.
password = []

# Boas vindas ao usuário.
print("Bem-vindo ao Gerador de Senhas!\n")

# Solicita ao usuário quantas letras deseja na senha.
num_letters = int(input("Quantas letras você gostaria em sua senha? \n"))
# Solicita ao usuário quantos símbolos deseja na senha.
num_symbols = int(input(f"Quantos símbolos você gostaria em sua senha? \n"))
# Solicita ao usuário quantos números deseja na senha.
num_numbers = int(input(f"Quantos números você gostaria em sua senha? \n"))

# Adiciona letras aleatórias da lista "letters".
for _ in range(num_letters):
    password.append(random.choice(letters))
# Adiciona símbolos aleatórios da lista "symbols".
for _ in range(num_symbols):
    password.append(random.choice(symbols))
# Adiciona números aleatórios da lista "numbers".
for _ in range(num_numbers):
    password.append(random.choice(numbers))

# Embaralha a lista.
random.shuffle(password)
# Transforma a lista "password" em uma string.
password = "".join(password)
# Exibe a senha para o usuário.
print(f"Sua senha é: {password}")
