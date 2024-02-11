from bs4 import BeautifulSoup
import requests
import smtplib

# Informações do usuário.
MY_EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR APP CODE"

# URL do produto na Amazon.
PRODUCT_URL = "https://www.amazon.com.br/Rel%C3%B3gio-Bolso-Technos-Ref-Grafite/dp/B07QSC5G84"

# Informações para enviar na solicitação da página.
headers = {
    "Accept-Language": "pt-BR,pt;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/109.0.0.0 Safari/537.36"
}

# Fazendo a solicitação.
response = requests.get(PRODUCT_URL, headers=headers)
# Processando o conteúdo da página.
soup = BeautifulSoup(response.content, "lxml")

# Extraindo o nome do produto.
product_name = f"{soup.find('span', id='productTitle').getText().strip('        ')}"
# Extraindo o preço do produto.
price = f"{soup.find('span', class_='a-offscreen').getText().strip('R$')}"

# Verifica se o preço é menor ou igual a um determinado valor.
if float(price.replace(',', '.')) <= 320:
    # Inicia a conexão com o servidor de email.
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        # Realiza login na conta de email do usuário.
        server.login(MY_EMAIL, PASSWORD)

        # Mensagem a ser enviada.
        message = f"Subject: Alerta de Preço na Amazon\n\n" \
                  f"O Produto {product_name} Está Por R${price}\n{PRODUCT_URL}"

        # Enviando o email.
        server.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.encode("utf8"))