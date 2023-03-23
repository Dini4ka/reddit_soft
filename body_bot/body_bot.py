import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from config import *

from time import sleep


class reddit_bot:
    def __init__(self):
        self.driver = uc.Chrome()

    def get_reddit(self):
        self.driver.get(AUTH_LINK)

    def auth(self):
        # Enter login and password
        self.driver.find_element(By.ID, 'loginUsername').send_keys(LOGIN)
        self.driver.find_element(By.ID, 'loginPassword').send_keys(PASSWD)

        # Clicking button
        self.driver.find_element(By.CSS_SELECTOR, '.m-full-width').click()
        sleep(4)

    def making_posts(self, title, post):
        # Going to the making_posts_field link
        self.driver.get(CREATE_POST_LINK)

        # Putting title
        self.driver.find_element(By.CSS_SELECTOR, '.PqYQ3WC15KaceZuKcFI02').send_keys(title)

        # Putting post's text
        self.driver.find_element(By.CSS_SELECTOR, '.notranslate').send_keys(post)

        # Clicking for post
        self.driver.find_element(By.CSS_SELECTOR, '._18Bo5Wuo3tMV-RDB8-kh8Z').click()

    def comment(self, post_link, comment_text):
        # Going to the post need comment
        self.driver.get(post_link)

        # Putting text of comment
        self.driver.find_element(By.CSS_SELECTOR, '.notranslate').send_keys(comment_text)

        # Press button for comment
        self.driver.find_element(By.CSS_SELECTOR, '._22S4OsoDdOqiM-hPTeOURa').click()
        time.sleep(2)
    def end(self):
        self.driver.close()


if __name__ == '__main__':
    bot = reddit_bot()
    bot.get_reddit()
    bot.auth()
    #bot.making_posts('Всем привет', 'Привет, ребята, я новенький! ')
    #bot.comment('https://www.reddit.com/r/marvelmemes/comments/11ysmwq/pour_one_out_for_all_the_bbegs_of_the_world/', 'Holly shit! ')
    bot.end()
