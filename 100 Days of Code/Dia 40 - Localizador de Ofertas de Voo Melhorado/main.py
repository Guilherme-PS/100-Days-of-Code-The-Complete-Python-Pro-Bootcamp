from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Código IATA da cidade de origem.
ORIGIN_CITY_IATA = "LON"

# Cria os objetos de gerenciamento de dados, busca de voo e notificação.
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Obtém dados das cidades de destino.
sheet_data = data_manager.get_destination_data()

# Se os códigos IATA das cidades de destino não estiverem preenchidos, busque-os.
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# Cria um dicionário com as informações das cidades de destino.
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# Define a data de amanhã e a data de seis meses a partir de hoje.
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# Loop para verificar os preços dos voos para cada cidade destino.
for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    # Se o voo não estiver disponível, pule.
    if flight is None:
        continue

    # Se o preço do voo for menor que o preço mais baixo salvo, envie notificações.
    if flight.price < destinations[destination_code]["price"]:

        # Obtém emails dos usuários.
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        # Se houver escalas, adiciona informação à mensagem.
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_emails(emails, message, link)
