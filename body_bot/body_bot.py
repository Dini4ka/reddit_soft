import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from config import *

from time import sleep


class reddit_bot:
    def __init__(self):
        self.driver = uc.Chrome()

    def get_reddit(self):
        self.driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

    def auth(self):
        # Enter login and password
        self.driver.find_element(By.ID, 'loginUsername').send_keys(LOGIN)
        self.driver.find_element(By.ID, 'loginPassword').send_keys(PASSWD)

        # Clicking button
        self.driver.find_element(By.CSS_SELECTOR, '.m-full-width').click()
        sleep(4)

    def end(self):
        self.driver.close()


if __name__ == '__main__':
    bot = reddit_bot()
    bot.get_reddit()
    bot.auth()
    bot.end()
