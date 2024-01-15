from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class VerbalMemoryBot:
    SCORE = 150       # Number of words to remember
    SEEN_WORDS = []   # List of words already seen

    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service())

    def initialize(self, btn_xpath):
        self.driver.get("https://humanbenchmark.com/tests/verbal-memory")
        self.driver.find_element(by=By.XPATH, value=btn_xpath).click()

    def logic(self, new_xpath, seen_xpath):
        for _ in range(self.SCORE):
            word = self.driver.find_element(by=By.XPATH, value="//*[@id=\"root\"]/div/div[4]/div[1]/div/div/div/div[2]/div")
            if word.text not in self.SEEN_WORDS:
                self.SEEN_WORDS.append(word.text)
                self.driver.find_element(by=By.XPATH, value=new_xpath).click()
            else:
                self.driver.find_element(by=By.XPATH, value=seen_xpath).click()

if __name__ == "__main__":
    btn_xpath = "//*[@id=\"root\"]/div/div[4]/div[1]/div/div/div/div[4]/button"
    new_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]'
    seen_xpath = '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]'

    bot = VerbalMemoryBot()
    bot.initialize(btn_xpath)
    bot.logic(new_xpath, seen_xpath)
