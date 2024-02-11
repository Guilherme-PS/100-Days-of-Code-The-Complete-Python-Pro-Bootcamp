from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# URL do Instagram.
INSTAGRAM_URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self, user, password, similar_account):
        """
        Construtor da classe InstaFollower.
        :param user: Nome de usuário para fazer login no Instagram.
        :param password: Senha para fazer login no Instagram.
        :param similar_account: Nome de usuário da conta que possui seguidores a serem seguidos.
        """
        self.service = Service("C:/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)

        self.user = user
        self.password = password
        self.similar_account = similar_account

    def login(self):
        """
        Realiza login no Instagram.
        """
        self.driver.get(INSTAGRAM_URL)
        sleep(3)

        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(self.user)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password, Keys.ENTER)
        sleep(5)

        try:
            self.driver.find_element(By.CLASS_NAME, "_ac8f").click()
        except NoSuchElementException:
            pass
        else:
            sleep(3)
        finally:
            self.driver.find_element(By.CLASS_NAME, "_a9_1").click()
            sleep(1)

    def find_followers(self):
        """
        Acessa a lista de seguidores da conta "similar_account".
        """
        self.driver.get(INSTAGRAM_URL + self.similar_account)
        sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, ".x1qjc9v5 ul li a").click()
        sleep(3)

        followers_div = self.driver.find_element(By.CLASS_NAME, "_aano")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_div)
            sleep(2)

    def follow(self):
        """
        Segue os usuários da conta "similar_account".
        """
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div div div button")

        for button in follow_buttons:
            if button.text == "Seguir":
                button.click()
                sleep(2)
