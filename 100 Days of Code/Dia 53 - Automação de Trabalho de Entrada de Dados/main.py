import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Configura o driver no navegador
driver_service = Service(executable_path="C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

# URL da Zillow e do formulário.
FORM_URL = "https://forms.gle/NVYMrHzCxk8t6SUG9"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.90678867945807%2C%22east%22%3A-122.22355929736328%2C%22south%22%3A37.61800246972393%2C%22west%22%3A-122.64653293017578%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# Cabeçalho da solicitação HTTP com informações do navegador e do idioma.
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.5",
}

# Fazendo a solicitação.
response = requests.get(ZILLOW_URL, headers=header)
# Processando o conteúdo da página.
soup = BeautifulSoup(response.text, "html.parser")

# Procura a lista de propriedades.
search = soup.find("ul", class_="List-c11n-8-84-2__sc-1smrmqp-0")

# Cria uma lista com os endereços.
adresses = [address.text.split(" | ")[-1] for address in search.find_all("address")]
# Cria uma lista com os preços por mês.
prices = [price.text.split("+")[0].replace("/mo", "") for price in search.find_all("div", class_="gugdBn")]
# Cria uma lista com os links.
url = "https://www.zillow.com"
links = [link["href"] if url in link["href"] else url + link["href"] for link in search.find_all("a", class_="cTLZKy")]

# Loop para iterar sobre as listas com o endereço, preços e links.
for adress, price, link in zip(adresses, prices, links):
    # Carrega a URL do formulário.
    driver.get(FORM_URL)
    # Pausa por 2 segundos para garantir que a página carregue.
    sleep(2)

    # Procura pelas caixas de texto e pelo botão de enviar.
    boxes = driver.find_elements(By.CLASS_NAME, "whsOnd")
    send_button = driver.find_element(By.CLASS_NAME, "l4V7wb")

    # Insere o endereço na primeira caixa.
    boxes[0].send_keys(adress)
    # Insere o preço na segunda caixa.
    boxes[1].send_keys(price)
    # Insere o link na terceira caixa.
    boxes[2].send_keys(link)

    # Clica no botão de enviar.
    send_button.click()