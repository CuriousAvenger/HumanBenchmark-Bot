from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://humanbenchmark.com/tests/verbal-memory")
driver.find_element(by=By.XPATH, value="//*[@id=\"root\"]/div/div[4]/div[1]/div/div/div/div[4]/button").click()
seen_words = []

for _ in range(150):
    word = driver.find_element(by=By.XPATH, value="//*[@id=\"root\"]/div/div[4]/div[1]/div/div/div/div[2]/div")
    if word.text not in seen_words:
        seen_words.append(word.text)
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
    else:
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()
