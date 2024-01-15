from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
from selenium.webdriver.chrome.service import Service

class TypingBot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service())

    def initialize(self):
        self.driver.get("https://humanbenchmark.com/tests/typing")

    def logic(self, text_xpath):
        text = self.driver.find_element(by=By.XPATH, value=text_xpath)
        pg.write(text.text)

if __name__ == "__main__":
    text_xpath = "//*[@id=\"root\"]/div/div[4]/div[1]/div/div[2]/div"

    bot = TypingBot()
    bot.initialize()
    bot.logic(text_xpath)