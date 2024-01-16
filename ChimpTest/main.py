from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains as ActionsChains

class ChimpTestBot:
    SCORE = 10
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service())
        self.actions = ActionsChains(self.driver)

    def initialize(self, btn_xpath):
        self.driver.get("https://humanbenchmark.com/tests/chimp")
        self.driver.find_element(by=By.XPATH, value=btn_xpath).click()
    
    def logic(self, next_xpath):
        for _ in range(self.SCORE-4):
            try:
                i = 1
                while True:
                    xpath = f'//div[@data-cellnumber="{i}"]'
                    element = self.driver.find_elements(by=By.XPATH, value=xpath)
                    self.actions.move_to_element(element[0]).click().perform()
                    i += 1
            except IndexError:
                i = 1
                self.driver.find_element(by=By.XPATH, value=next_xpath).click()

if __name__ == "__main__":
    btn_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/button'
    next_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button'

    bot = ChimpTestBot()
    bot.initialize(btn_xpath)
    bot.logic(next_xpath)