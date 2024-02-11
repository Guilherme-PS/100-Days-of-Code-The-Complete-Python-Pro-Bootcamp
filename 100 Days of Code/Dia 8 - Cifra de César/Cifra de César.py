def caesar(direction_choice: str, user_text: str, shift_amount: int, letters: list) -> str:
    """
    Codifica ou decodifica um texto utilizando a Cifra de César.
    :param direction_choice: "encode" ou decode".
    :param user_text: Texto a ser codificado ou decodificado.
    :param shift_amount: Valor para deslocar as letras.
    :param letters: Alfabeto a ser usado para a codificação ou decodificação.
    :return: Texto codificado ou decodificado.
    """
    final_text = ""
    direction_name = "codificado"

    if direction_choice == "decode":
        direction_name = "decodificado"
        shift_amount *= -1

    for letter in user_text:
        if letter in letters:
            position = letters.index(letter) + shift_amount

            if position > len(alphabet) - 1:
                final_text += letters[position % len(letters)]
            else:
                final_text += letters[position % len(letters)]

        else:
            final_text = ""
            for char in user_text:
                if char in letters:
                    final_text += "*"
                else:
                    final_text += char
            break

    return f"O texto {direction_name} é: {final_text}\n"

def new_word():
    """
    Pergunta ao usuário se ele deseja continuar ou sair do programa.
    """
    while True:
        answer = input("Deseja Continuar? [S/N] ").upper()

        if answer == "S":
            break
        elif answer == "N":
            exit()
        else:
            print("Opção Inválida!")


# Lista com as letras do alfabeto.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while True:
    # Solicita ao usuário que escolha entre criptografar e descriptografar.
    direction = input("Digite [encode] para criptografar, digite [decode] para descriptografar:\n").lower()
    # Solicita ao usuário uma mensagem.
    text = input("Digite sua mensagem:\n").lower()
    # Solicita ao usuário uma chave para criptografar ou descriptografar.
    shift = int(input("Digite a chave:\n"))
    # Aplica a função na palavra solicitada e a retorna.
    print(caesar(direction_choice=direction, user_text=text, shift_amount=shift, letters=alphabet))
    # Pergunta ao o usuário se ele deseja codificar ou decodificar uma palavra novamente.
    new_word()