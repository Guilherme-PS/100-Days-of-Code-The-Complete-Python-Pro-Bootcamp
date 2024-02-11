import requests
from twilio.rest import Client

# Nome da empresa.
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# ID e Auth Token do Twilio.
TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Alpha Vantage API.
ALPHA_VANTAGE_API_KEY = "YOUR ALPHA VANTAGE KEY"
# Parâmetros da API Alpha Vantage.
alpha_vantage_parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": STOCK, "apikey": ALPHA_VANTAGE_API_KEY}

# Faz a solicitação à API Alpha Vantage.
alpha_vantage_response = requests.get("https://www.alphavantage.co/query", params=alpha_vantage_parameters)
# Verifica se a resposta foi bem-sucedida.
alpha_vantage_response.raise_for_status()

# Define o preço de fechamento de ontem.
yesterday = float(list(alpha_vantage_response.json()["Time Series (Daily)"].values())[0]["4. close"])
# Define o preço de fechamento do dia anterior.
day_before_yesterday = float(list(alpha_vantage_response.json()["Time Series (Daily)"].values())[1]["4. close"])

# Calcula a diferença entre os dois preços
diff = yesterday - day_before_yesterday

# Define a seta para cima ou para baixo se a diferença for positiva ou negativa.
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Calcula a diferença percentual.
percent = round((diff / yesterday) * 100)

# Verifica se a diferença percentual é maior ou igual a 5%.
if abs(percent) >= 5:
    NEWS_API_API_KEY = "YOUR NEWS API KEY"
    # Define os parãmetros para API News.
    news_api_parameters = {"q": COMPANY_NAME,
                           "from": list(alpha_vantage_response.json()["Time Series (Daily)"].keys())[0],
                           "sortBy": "popularity", "apiKey": NEWS_API_API_KEY}

    # Faz a solicitação à API News.
    news_api_response = requests.get("https://newsapi.org/v2/everything", params=news_api_parameters)
    # Verifica se a resposta foi bem-sucedida.
    news_api_response.raise_for_status()
    news_api_data = news_api_response.json()['articles']

    # Cria uma instância do cliente Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    # Mensagem.
    formatted_message = [f"{STOCK}: {up_down}{percent}%\nHeadline: {news_api_data[0]['title']}\nBrief: {news_api_data[0]['description']}",
                         f"Headline: {news_api_data[1]['title']}\nBrief: {news_api_data[1]['description']}"]

    # Envia um SMS avisando se a ação subiu ou desceu e dois artigos para o usuário.
    for article in formatted_message:
        message = client.message.create(body=article,
                                        from_="TWILIO NUMBER",
                                        to="YOUR NUMBER")



