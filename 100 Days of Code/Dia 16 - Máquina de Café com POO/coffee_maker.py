class CoffeeMaker:
    """Modela a máquina que faz o café"""
    def __init__(self):
        self.resources = {
            "água": 300,
            "leite": 200,
            "café": 100,
        }

    def report(self):
        """Imprime um relatório de todos os recursos."""
        print(f"Água: {self.resources['água']}ml")
        print(f"Leite: {self.resources['leite']}ml")
        print(f"Café: {self.resources['café']}g")

    def is_resource_sufficient(self, drink):
        """Retorna True quando o pedido pode ser feito, False se os ingredientes são insuficientes."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Desculpe, não há {item} o suficiente.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deduz os ingredientes necessários dos recursos."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aqui está o seu {order.name} ☕.\nAproveite!")