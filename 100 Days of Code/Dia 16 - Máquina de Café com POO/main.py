# Importando as funções necessárias para a máquina de café.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Loop infinito
while True:
    # Solicita ao usuário que escolha um café.
    order = input(f"O que você gostaria? /{menu.get_items().title()}: ").title()

    # Retorna os ingredientes e o dinheiro que a máquina possui.
    if order == "Report":
        coffee_maker.report()
        money_machine.report()

    # Finaliza o programa (desliga a máquina).
    elif order == "Off":
        print("Desligando a Máquina...")
        break

    # Verifica tem o pedido na máquina.
    elif menu.find_drink(order):
        # Verifica se os ingredientes são o suficiente para fazer o café.
        if coffee_maker.is_resource_sufficient(menu.find_drink(order)):
            # Verifica o pagamento e retorna o troco se necessário.
            if money_machine.make_payment(menu.find_drink(order).cost):
                coffee_maker.make_coffee(menu.find_drink(order))