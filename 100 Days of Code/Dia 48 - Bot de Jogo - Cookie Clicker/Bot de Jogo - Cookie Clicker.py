from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import time

# Cria a instância do serviço de driver do Chrome.
driver_service = Service(executable_path="C:/Development/chromedriver.exe")
# Cria a instância do driver do Chrome.
driver = webdriver.Chrome(service=driver_service)

# Abre a página do jogo.
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Encontra o elemento que representa o cookie.
cookie = driver.find_element(By.ID, "cookie")

# Inicializa variáveis para controlar a exibição de CPS e a compra de melhorias.
cps_check = time.time() + 300
buy_upgrade = time.time() + 5

# Loop infinito.
while True:
    # Clica no cookie.
    cookie.click()

    # Verifica se é hora de exibir o CPS
    if time.time() > cps_check:
        print(driver.find_element(By.ID, "cps").text)
        cps_check = time.time() + 300

    # Verifica se é hora de comprar melhorias.
    if time.time() > buy_upgrade:
        # Encontra todos os itens da loja.
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")[1::]

        # Percorre os itens da loja de trás pra frente.
        for item in store[::-1]:
            # Verifica se o item não está desativado.
            if item.get_attribute("class") != "grayed":
                try:
                    # Tenta clicar no item.
                    item.click()
                except ElementNotInteractableException:
                    # Se não puder clicar, continua a iteração.
                    continue

                # Encontra o CPDS atual
                cps = driver.find_element(By.ID, "cps").text.split()[-1]

                # Converte o CPS para float.
                try:
                    cps = float(cps)
                except ValueError:
                    cps = float(cps.replace(",", ""))

                # Atualiza a variável que controla o tempo de compra de melhorias de acordo com o CPS atual.
                if cps >= 1000:
                    buy_upgrade = time.time() + 25
                elif cps >= 750:
                    buy_upgrade = time.time() + 20
                elif cps >= 500:
                    buy_upgrade = time.time() + 15
                elif cps >= 250:
                    buy_upgrade = time.time() + 10
                else:
                    buy_upgrade = time.time() + 5

                # Para de procurar upgrades.
                break