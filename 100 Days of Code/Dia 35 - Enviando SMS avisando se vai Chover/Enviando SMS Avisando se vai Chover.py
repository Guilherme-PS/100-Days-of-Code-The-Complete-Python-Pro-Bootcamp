# IMPORTANTE! Para que o código funcione, você precisa substituir todos os espaços reservados com seus próprios dados.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Endpoint da API do OpenWeatherMap
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# Lendo a chave da API do OpenWeatherMap de uma variável de ambiente.
api_key = os.environ.get("OWM_API_KEY")
# Armazenando o SID da conta do Twilio.
account_sid = "YOUR ACCOUNT SID"
# Lendo o token de autenticação do Twilio de uma variável de ambiente.
auth_token = os.environ.get("AUTH_TOKEN")

# Parâmetros da requisição à API do OpenWeatherMap.
weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# Fazendo a requisição à API e ver ificando se houve erro.
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# Acessando a informação de previsão de chuva nas próximas 12 horas.
data_sliced = response.json()["hourly"][:12]

# Inicializando a variável que indica se vai chover.
will_rain = False

# Verificando se vai chover nas próximas 12 horas.
for hour_data in data_sliced:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# Se chover, envia a mensagem de texto.
if will_rain:
    # Criando um cliente HTTP`para usar um proxy.
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    # Enviando a mensagem de texto.
    message = client.messages \
        .create(body="Vai chover hoje. Lembre-se de levar um ☔️",
                from_="YOUR TWILIO VIRTUAL NUMBER",
                to="YOUR TWILIO VERIFIED REAL NUMBER")

    # Imprimindo o status da mensagem enviada
    print(message.status)
