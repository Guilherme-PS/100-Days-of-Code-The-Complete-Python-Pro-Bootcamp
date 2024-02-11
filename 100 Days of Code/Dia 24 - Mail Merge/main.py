# ABre o arquivo "invited_names.txt" no modo de leitura.
with open("./Input/Names/invited_names.txt", mode="r") as names:
    # Lendo as linhas do arquivo e armazenando em uma lista.
    invited_names = names.readlines()

# Abre o arquivo "starting_letter.txt" no modo de leitura.
with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    # Lendo todo o conteúdo do arquivo e armazenando em um variável.
    letters = letter.read()

    # Iterando sobre cada nome da lista de convidados.
    for name in invited_names:
        # Substitui o placeholder "[name]" pelo nome do convidado.
        letter_for = letters.replace("[name],", F"{name.strip()},")

        # Cria um arquivo e abre ele em modo de escrita.
        with open(f"./Output/ReadyToSend/Letter_for_{name.strip()}.txt", mode="w") as ready_letter:
            # Escreve cada linha no arquivo novo.
            for line in letter_for:
                ready_letter.write(line)