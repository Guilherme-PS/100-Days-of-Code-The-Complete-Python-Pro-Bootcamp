def highest_bid(bids_dict: dict) -> str:
    """
    Retorna o nome do vencedor e o valor da maior proposta em um leilão.
    :param bids_dict: Dicionário de ofertas, onde as chaves são os nomes dos participantes e os valores são as ofertas.
    :return: Uma string indicando o nome do vencedor e o valor da maior oferta.
    """
    winner, high_bid = "", 0

    for key, value in bids_dict.items():
        if value > high_bid:
            winner, high_bid = key, value

    return f"O ganhador é: {winner}, com uma oferta de: R${high_bid:,.2f}!"


# Boas vindas ao usuário.
print("Bem-vindo ao Programa de Leilões Secretos!\n")
# Criando o dicionário de ofertas vazio
bids = dict()

# Variável responsável por manter o loop.
others_bidders = "S"
while others_bidders == "S":
    # Solicita ao usuário o seu nome.
    name = input("Qual o seu nome?: ").title()
    # Solicita ao usuário a oferta.
    bid = float(input("Qual a sua oferta?: R$"))

    # Adiciona o nome e a oferta no dicionário "bids".
    bids[name] = bid

    # Pergunta ao usuário se possui mais participantes. Se não, interrompe o loop.
    others_bidders = input("Existem outros participantes? [S/N]\n").upper()

# Verifica qual a maior oferta.
print(highest_bid(bids))