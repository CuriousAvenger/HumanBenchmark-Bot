from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pyautogui as pg

class NumberMemoryBot:
    SCORE = 25       # Number of numbers to remember
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service())

    def initialize(self, btn_xpath):
        self.driver.get("https://humanbenchmark.com/tests/number-memory")
        self.driver.find_element(by=By.XPATH, value=btn_xpath).click()

    def logic(self, num_xpath, form_xpath, submit_xpath, next_xpath):
        for _ in range(self.SCORE):
            num = self.driver.find_element(by=By.XPATH, value=num_xpath).text
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, form_xpath)))

            pg.write(num)
            self.driver.find_element(by=By.XPATH, value=submit_xpath).click()
            self.driver.find_element(by=By.XPATH, value=next_xpath).click()

if __name__ == "__main__":
    btn_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button'
    num_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]'
    form_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input'
    submit_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button'
    next_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button'

    bot = NumberMemoryBot()
    bot.initialize(btn_xpath)
    bot.logic(num_xpath, form_xpath, submit_xpath, next_xpath)