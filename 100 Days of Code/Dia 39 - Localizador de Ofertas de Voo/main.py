from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Objeto de gerenciamento de dados.
data_manager = DataManager()
# Dados do google sheet.
sheet_data = data_manager.get_destination_data()
# Objeto de busca de passagens aéreas.
flight_search = FlightSearch()
# Objeto de gerenciamento de notificações.
notification_manager = NotificationManager()

# Armazena o código IATA da cidade de origem.
ORIGIN_CITY_IATA = "RIO"

# Verifica se a coluna "IATA Code" está vazia.
if sheet_data[0]["iataCode"] == "":
    # Preenchendo a coluna com o código IATA das cidades.
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # Atualiza a planilha de dados com os novos códigos.
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Armazenando a data de amanhã e a de seis meses a partir de hoje.
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Loop para verificar os preços das passagens para cada destino.
for destination in sheet_data:
    # Verificando preços das passagens usando o objeto flight_search.
    flight = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], from_time=tomorrow,
                                         to_time=six_month_from_today)

    # Verifica se o preço da passagem é menor do que o preço mais baixo ja registrado para esse destino>
    if flight.price < destination["lowestPrice"]:
        # Enviando um SMS usando o objeto de notification_manager
        notification_manager.send_sms(message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-"
                                              f"{flight.origin_airport} to {flight.destination_city}-"
                                              f"{flight.destination_airport}, from {flight.out_date} "
                                              f"to {flight.return_date}.")

