    import requests
import datetime as dt
import smtplib
import time

# Adicione suas credenciais de email e senha de app.
MY_EMAIL = "SEU EMAIL"
PASSWORD = "SENHA DE APP"

# Adicione sua latitude e longitude.
MY_LATITUDE = -22.597231  # SUA LATITUDE
MY_LONGITUDE = -43.691730  # SUA LONGITUDE

def iss_overhead():
    """
    Verifica se a ISS está sobrevoando uma determinada área.
    Ela faz uma requsição à API "http://api.open-notify.org/iss-now.json" para obter a posição atual da ISS.
    Em se, ela verifica se a latitude e longitude da ISS estão dentro da latitude e longitude do usuário.
    Se estiverem retorna True ou False.
    :return: True ou False.
    """
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    return MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE - 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE - 5

def is_night():
    """
    Verifica se é noite na latitude e longitude do usuário.
    Ela faz uma requisição à API "https://api.sunrise-sunset.org/json" com os parâmetros "lat" (latitude),
    "lng" (longitude) e "formatted" (formato de data) para obter informações sobre o horário do nascer e pôr do sol.
    Em seguida verifica se o horário atual está entre esses dois horários, caso esteja, a função retorna True, caso contrário,
    False.
    :return: True ou False.
    """
    parameters = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE, "formatted": 0}

    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()

    sunrise_data = int(sunset_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_data = int(sunset_response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now()

    return now.hour >= sunset_data or now.hour <= sunrise_data


# Loop infinito
while True:
    # Verifica se é noite e se a ISS está próxima a longitude e latitude do usuário.
    if iss_overhead() and is_night():
        # Envia um email para o usuário
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user=MY_EMAIL, password=PASSWORD)

            # Mensagem de aviso.
            message = "Subject:Olhe Para Cima\n\n" \
                      "A Estação Espacial Internacional está passando diretamente sobre a sua localização."

            # Enviando o email.
            server.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=message.encode("utf8"))

    # Pausa o loop por 60 segundos antes de verificar novamente.
    time.sleep(60)