from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# URL do Twitter e do Speedtest.
TWITTER_URL = "https://twitter.com/i/flow/login"
SPEEDTEST_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self, user, password, internet_speed):
        """
        Inicia a classe InternetSpeedTwitterBot.
        :param user: Usuário do Twitter.
        :param password: Senha do Twitter.
        :param internet_speed: Tupla contendo a velocidade de download e upload contratadas pelo usuário.
        """
        self.driver_service = Service(executable_path="C:/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_service)

        self.speed = (None, None)
        self.internet_speed = internet_speed

        self.user = user
        self.password = password

    def get_internet_speed(self):
        """
        Obtém a velocidade de download e upload da internet.
        :return: A velocidade da internet.
        """
        self.driver.get(SPEEDTEST_URL)

        sleep(5)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CLASS_NAME, "start-text").click()

        sleep(5)

        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")

        while download_speed.text == "--" or upload_speed.text == "--":
            download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
            upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        else:
            sleep(3)
            self.speed = (float(download_speed.text), float(upload_speed.text))
            return self.speed

    def tweet_internet_speed(self):
        """
        Faz um tweet questionando o provedor de internet caso a velocidade da internet seja menor que a contratada.
        """
        if self.speed[0] < self.internet_speed[0] and self.speed[1] < self.internet_speed[1]:
            self.driver.get(TWITTER_URL)
            sleep(3)

            user = self.driver.find_element(By.NAME, "text")
            user.send_keys(self.user, Keys.ENTER)

            sleep(3)

            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(self.password, Keys.ENTER)

            sleep(3)

            message = f"Ei, provedor! Gostaria de entender por que minha velocidade de download está atualmente " \
                      f"em {self.speed[0]} Mbps e a velocidade de upload em {self.speed[1]} Mbps, se eu pago " \
                      f"por um pacote de {self.internet_speed[0]} Mbps de download e {self.internet_speed[1]} " \
                      f"Mbps de upload?"

            tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
            tweet.send_keys(message)
            sleep(3)

            make_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                            'div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                            'div[3]/div/div/div[2]/div[3]/div/span/span')
            make_tweet.click()
            sleep(5)


