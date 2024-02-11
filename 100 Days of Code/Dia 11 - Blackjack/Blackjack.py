# Importa o módulo random.
import random

def deal_cards(hand: list) -> list:
    """
    Coloca uma carta aleatória na mão do jogador.
    :param hand: Mão atual do jogador.
    :return: Mão do jogador com uma carta atual.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))

    return hand

def calculate_hand(hand: list) -> int:
    """
    Calcula o valor da mão do jogador de acordo com as regras do Blackjack.
    :param hand: Mão atual do jogador.
    :return: Valor da mão do jogador.
    """
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1

    return sum(hand)

def play_blackjack():
    """
    Inicia o blackjack.
    """
    player_hand = list()
    computer_hand = list()

    player_bool = True
    computer_bool = True

    for _ in range(2):
        deal_cards(player_hand)
        deal_cards(computer_hand)

    while player_bool or computer_bool:
        if player_bool:
            print(f"\n\tSuas Cartas: {player_hand}, Valor Atual: {calculate_hand(player_hand)}")
            print(f"\tPrimeira Carta do Oponente: [{computer_hand[0]}]")

            answer = input("Digite [Hit] para obter uma carta, digite [Stand] para passar: ").title()

            if answer == "Stand":
                player_bool = False
            else:
                deal_cards(player_hand)

        if computer_bool:
            if calculate_hand(computer_hand) > 17:
                computer_bool = False
            else:
                deal_cards(computer_hand)

        if (calculate_hand(player_hand) >= 21) or (calculate_hand(computer_hand) >= 21):
            break

    if calculate_hand(player_hand) == calculate_hand(computer_hand):
        winner = "Empate!"

    elif calculate_hand(player_hand) == 21:
        winner = "Você Ganhou!"
    elif calculate_hand(player_hand) > 21:
        winner = "Você Perdeu."

    elif calculate_hand(computer_hand) == 21:
        winner = "Você Perdeu."
    elif calculate_hand(computer_hand) > 21:
        winner = "Você Ganhou!"

    elif calculate_hand(player_hand) > calculate_hand(computer_hand):
        winner = "Você Ganhou!"
    else:
        winner = "Você Perdeu."

    print(f"{winner}\n\nSua mão: {player_hand}, Pontuação Final: {calculate_hand(player_hand)}")
    print(f"Mão do computador: {computer_hand}, Pontuação Final: {calculate_hand(computer_hand)}")


# Mantém o jogo em loop.
while input("Você quer jogar uma partida de Blackjack? [S/N] ").upper() == "S":
    # Inicia o jogo.
    play_blackjack()