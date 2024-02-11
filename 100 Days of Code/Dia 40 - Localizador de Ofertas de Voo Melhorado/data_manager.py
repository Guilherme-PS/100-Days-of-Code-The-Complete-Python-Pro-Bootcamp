from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT
SHEETY_USERS_ENDPOINT = YOUR SHEETY USERS ENDPOINT

class DataManager:
    def __init__(self):
        """
        Construtor da classe, inicializa um dicionário vazio para armazenar informações de destino.
        """
        self.destination_data = {}

    def get_destination_data(self):
        """
        Obtém os dados dos destinos através de uma requyisição GET para a API Sheety Prices e armazena em
        self.destination_data.
        :return: Dados dos destinos.
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """
        Atualiza os códigos IATA dos destinos através de requisições PUT para a API Sheety Prices.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        """
        Obtém os emails dos clientes através de uma requisição GET para a API Sheety Users e armazena em
        self.customer_data.
        :return: Emails dos usuários.
        """
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data