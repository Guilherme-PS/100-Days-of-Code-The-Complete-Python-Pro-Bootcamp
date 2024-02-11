class MenuItem:
    """Modela cada item de menu."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "água": water,
            "leite": milk,
            "café": coffee
        }


class Menu:
    """Modela o Menu com bebidas."""
    def __init__(self):
        self.menu = [
            MenuItem(name="Café Com Leite", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="Cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Retorna todos os nomes dos itens de menu disponíveis."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Procura no menu uma bebida específica pelo nome. Retorna esse item se ele existir, caso contrário,
        retorna None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Desculpe, esse item não está disponível.")