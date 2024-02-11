class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Imprime o lucro atual"""
        print(f"Dinheiro: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Retorna o total calculado a partir das moedas inseridas."""
        print("Por favor, insira as moedas.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Quantos {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Retorna True quando o pagamento é aceito, ou False se insuficiente."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Aqui está o seu troco: {self.CURRENCY}{change}.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Desculpe, o dinheiro não é o suficiente.\nReembolsando o Dinheiro...")
            self.money_received = 0
            return False