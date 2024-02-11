from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# Constantes com o email e senha do LinkedIn.
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

# Define o serviço do webdriver Chrome.
driver_service = Service(executable_path="C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

# Abre o LinkedIn no navegador.
driver.get("https://www.linkedin.com")

# Preenche o email e senha nas caixas correspondentes e faz o login.
email = driver.find_element(By.ID, "session_key")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "session_password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Aguarda 15 segundos para garantir que a página carregue completamente.
sleep(15)

# Abre a páginade busca de vagas do LinkedIn para desenvolvedores Python no Rio de Janeiro.
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Rio%20de%20Janeiro%2C%20Rio%20de%"
           "20Janeiro%2C%20Brasil&geoId=106701406&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

# Aguarda 5 segundos para a página carregar completamente.
sleep(5)

# Encontra os resultados de busca de vagas e itera sobre eles.
results = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for job in results:
    try:
        # Clica na vaga e aguarda 10 segundos para que a página carregue completamente.
        job.click()
        driver.execute_script("arguments[0].scrollIntoView();", job)
        sleep(10)

        # Verifica se a vaga não foi salva.
        if driver.find_element(By.CLASS_NAME, "jobs-save-button span").text.split("\n")[0] == "Salvar":
            # Salva a vaga.
            driver.find_element(By.CLASS_NAME, "jobs-save-button").click()

            # Verifica se a empresa ainda não está sendo seguida.
            if driver.find_element(By.CLASS_NAME, "follow span").text == "Seguir":
                driver.execute_script("arguments[0].scrollIntoView();", job)
                # Segue a empresa.
                driver.find_element(By.CLASS_NAME, "follow").click()
                sleep(5)
        else:
            continue

    except NoSuchElementException:
        continue

# Fecha o navegador.
driver.quit()