from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pyautogui as pg

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://humanbenchmark.com/tests/number-memory")
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button').click()

for _ in range(25):
    num = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]').text
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input')))

    pg.write(num)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button').click()
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()