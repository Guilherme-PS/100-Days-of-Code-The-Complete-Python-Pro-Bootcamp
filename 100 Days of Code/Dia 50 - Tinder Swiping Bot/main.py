from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

# Constantes com a URL do Tinder e os dados do usuário.
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
TINDER_URL = "https://tinder.com/"

# Configura o driver no navegador
service = Service(executable_path="C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Acessa o Tinder.
driver.get(TINDER_URL)
sleep(1)

# Aceita termos de privacidade.
driver.find_element(By.XPATH, '//*[@id="o-1180012777"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]').click()

# Procura e clica no botão "Entre"
driver.find_element(By.XPATH, '//*[@id="o-1180012777"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]'
                              '/div[2]/a/div[2]/div[2]').click()
sleep(1)
# Seleciona a opção "Entrar com o Facebook".
driver.find_element(By.XPATH, '//*[@id="o-958672341"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]'
                              '/div[2]').click()
sleep(2)

# Muda para a nova janela aberta.
windows = driver.window_handles
driver.switch_to.window(windows[1])

# Preenche os campos de email e senha.
email = driver.find_element(By.NAME, "email")
email.send_keys(EMAIL)
password = driver.find_element(By.NAME, "pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Volta para a janela principal.
driver.switch_to.window(windows[0])

# Espera 10 segundos para o site carregar completamente.
sleep(10)
# Clica nos botões "Permitir" e "Não".
driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="q-184954025"]/div/div[2]/div/div/div[1]/button').click()
sleep(5)

# Clica no botão "Não" novamente.
driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[2]').click()
sleep(5)

# Loop principal com o número máximo de matches a serem obtidos (usuários free).
for num in range(100):
    sleep(3)
    try:
        # Verifica se há um pop-up na tela e clica no botão "Não".
        pop_up = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[2]/button[2]')
        pop_up.click()
    except Exception as error:
        pass
    except ElementClickInterceptedException:
        # Clica no botão "Eu aceito" se houver um pop-up de "Match".
        driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
    finally:
        # Clica na seta para ir para o próximo perfil.
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT).perform()