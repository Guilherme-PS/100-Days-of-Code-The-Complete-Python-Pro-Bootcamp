import requests
import datetime as dt

# Dados do usuário.
APP_ID = "SEU ID"
API_KEY = "SUA CHAVE"

# Solicita ao usuário que ele informe qual exercício ele fez e armazena essa informação em um dicionário.
parameters = {"query": input("Tell me which exercises you did? ")}
# Adiciona os dados do usuário em um dicionário.
header = {"x-app-id": APP_ID, "x-app-key": API_KEY}

# Faz uma solicitação POST com os parâmetros e cabeçalhos especificados.
response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=header)

# Acessa os dados da resposta e os armazena em uma variável.
exercises_data = response.json()["exercises"]

# Cria um dicionário.
google_sheets_data = {"workout": {}}

# Para cada dado de exercício no dicionário "exercises_data".
for data in exercises_data:
    # Armazena a data e o horário atual.
    today = dt.datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")

    # Preenche o dicionário com a data, hora e as informações sobre os exercícios.
    google_sheets_data["workout"] = {"date": date, "time": time, "exercise": data["name"].title(),
                                     "duration": f"{round(data['duration_min'])} min",
                                     "calories": f"{round(data['nf_calories'])} kcal"}

# Variável da SHEETY API com o link do usuário.
SHEETY_API_LINK = "SEU LINK"

# Envia o dicionário com as informações para o google sheets.
sheety_post = requests.post(SHEETY_API_LINK, json=google_sheets_data)


