from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class ReactionTimeBot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service())

    def initialize(self, btn_class):
        self.driver.get("https://humanbenchmark.com/tests/reactiontime")
        self.driver.find_element(by=By.CLASS_NAME, value=btn_class).click()

    def logic(self, green_class, cont_class):
        for _ in range(5):
            while True:
                try:
                    self.driver.find_element(by=By.CLASS_NAME, value=green_class).click()                
                    self.driver.find_element(by=By.CLASS_NAME, value=cont_class).click()
                except Exception:
                    continue

if __name__ == "__main__":
    btn_class = 'view-splash'
    green_class = 'view-go'
    cont_class = 'view-result'

    bot = ReactionTimeBot()
    bot.initialize(btn_class)
    bot.logic(green_class, cont_class)