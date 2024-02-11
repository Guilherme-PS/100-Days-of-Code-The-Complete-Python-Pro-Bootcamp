MENU = {
    "Espresso": {
        "ingredients": {
            "água": 50,
            "leite": 0,
            "café": 18,
        },
        "cost": 1.5,
    },
    "Café Com Leite": {
        "ingredients": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "água": 300,
    "leite": 200,
    "café": 100,
}


def process_coins():
    """
    Recebe uma quantidade de moedas e retorna o valor total em dólares.
    :return: Valor total em doláres.
    """
    print("\nPor favor, insira as moedas.")

    total_value = 0
    for coin, value in {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}.items():
        total_value += int(input(f"Quantos {coin.title()}?: ")) * value

    return total_value


def check_resources(coffee):
    """
    Verifica se há ingredientes o suficiente para fazer o café.
    :param coffee: Café a ser verificado.
    :return: True se houver ingredientes e False se não tiver, caso contrário retorna uma mensagem dizendo que o
    item não foi encontrado.
    """
    if coffee in MENU.keys():
        can_make = True
        for resource, quantity in MENU[coffee]["ingredients"].items():
            if resources[resource] < quantity:
                print(f"Desculpe, não há {resource.title()} o suficiente.")
                can_make = False

        return can_make
    else:
        print("Desculpe, esse item não está disponível.")


def preparing_coffee(coffee):
    """
    Prepara o café especificado.
    :param coffee: Café a ser preparado
    :return: None
    """
    for resource in MENU[coffee]["ingredients"].keys():
        resources[resource] -= MENU[coffee]["ingredients"][resource]

    print(f"\nAqui está o seu {coffee} ☕ Aproveite!")


# Dinheiro da máquina
profit = 0

# Loop infinito
while True:
    # Solicita ao usuário que escolha um café.
    order = input("O que você gostaria? [Espresso/Café Com Leite/Cappuccino]?: ").title()

    # Retorna os ingredientes e o dinheiro que a máquina possui.
    if order == "Report":
        for ingredient, amount in resources.items():
            if ingredient == "café":
                print(f"{ingredient.title()}: {amount}g")
            else:
                print(f"{ingredient.title()}: {amount}ml")
        print(f"Dinheiro: ${profit:.2f}")

    # Finaliza o programa (desliga a máquina).
    elif order == "Off":
        print("Desligando a Máquina...")
        break

    # Verifica se possui todos os ingredientes necessários para fazer o café.
    elif check_resources(order):
        payment = process_coins()

        # Verifica se o pagamento está correto.
        if payment >= MENU[order]["cost"]:
            profit += MENU[order]["cost"]
            # Retorna o troco se necessário.
            if payment > MENU[order]["cost"]:
                print(f"Aqui está o seu troco: ${payment - MENU[order]['cost']:.2f}")
            # Prepara o café.
            preparing_coffee(order)
        # Devolve o dinheiro ao usuário caso não seja o suficiente.
        else:
            print("\nDesculpe, não há dinheiro o suficiente.\nReembolsando o Dinheiro...")