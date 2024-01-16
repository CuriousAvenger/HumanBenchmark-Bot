from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains as ActionsChains

class AimTrainerBot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service())
        self.actions = ActionsChains(self.driver)

    def initialize(self, btn_xpath):
        self.driver.get("https://humanbenchmark.com/tests/aim")
        element = self.driver.find_element(by=By.XPATH, value=btn_xpath)
        self.actions.move_to_element(element).click().perform()
    
    def logic(self, target_xpath):
        for _ in range(30):
            element = self.driver.find_element(by=By.XPATH, value=target_xpath)
            self.actions.move_to_element(element).click().perform()

if __name__ == "__main__":
    btn_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[2]'
    target_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div/div/div[2]'

    bot = AimTrainerBot()
    bot.initialize(btn_xpath)
    bot.logic(target_xpath)



# 