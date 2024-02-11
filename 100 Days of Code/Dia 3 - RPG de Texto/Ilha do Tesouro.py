print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Boas vindas ao jogador e mostra qual o objetivo do jogo.
print(f"Bem-vindo ao Jogo: Ilha do Tesouro!")
print("Objetivo: Encontrar o Tesouro.\n")

# Solicita ao jogador que escolha um caminho para seguir.
road_choice = input("Você está em uma bifurcação. Para qual lado você quer ir? [Esquerda] ou [Direita]:\n").title()

# Verifica a escolha do jogador.
if road_choice == "Esquerda":
    # Solicita ao jogador como ele deve atravessar o lago.
    lake_choice = input("Você se depara com um lago e, no centro dele, há uma ilha. "
                        "[Esperar] para esperar por um barco. [Nadar] para atravessar nadando.\n").title()
    # Verifica a escolha do jogador.
    if lake_choice == "Esperar":
        # Solicita ao jogador que ele escolha uma das portas.
        door_choice = input("Após chegar a ilha, você percebe que há uma casa com três portas à sua frente. "
                            "Uma [Vermelho Escuro], uma [Amarela] e uma [Azu]. Qual porta você escolhe?\n").title()
        # Vitória
        if door_choice == "Vermelho Escuro":
            print("Ao abrir a porta, você é recompensado com a visão de um tesouro brilhante e valioso.\nVocê Ganhou!")
        # Fim de jogo
        elif door_choice == "Azul":
            print("Ao abrir a porta, você é recebido por uma multidão de criaturas selvagens.\nFim de Jogo.")
        # Fim de jogo
        else:
            print("Ao abrir a porta, você é atingido por uma flecha.\nFim de Jogo.")
    # Fim de jogo
    else:
        print("Enquanto nadava pelo lago, você é atacado por um tubarão-branco.\nFim de Jogo.")
# Fim de jogo
else:
    print("Enquanto andava, você acaba caindo em um buraco escondido no chão.\nFim de Jogo.")