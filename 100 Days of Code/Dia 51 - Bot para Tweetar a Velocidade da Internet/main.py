from internet_speed_twitter_bot import InternetSpeedTwitterBot

# Define o nome de usuário e senha do Twitter.
TWITTER_USER = "YOUR TWITTER USER"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"

# Define a velocidade de internet contratada subtraindo 1 da velocidade real.
INTERNET_SPEED = (15.0 - 1, 5.0 - 1)  # Download - 1 / Upload - 1

# Cria uma instância do objeto InternetSpeedTwitterBot com os parâmetros específicados.
bot = InternetSpeedTwitterBot(user=TWITTER_USER, password=TWITTER_PASSWORD, internet_speed=INTERNET_SPEED)

# Chama o método "get_internet_speed()" para medir a velocidade da internet.
bot.get_internet_speed()
# Chama o método "tweet_internet_speed()" para enviar um tweet caso a velocidade da internet seja inferior à contratada.
bot.tweet_internet_speed()






