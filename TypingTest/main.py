from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui as pg

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://humanbenchmark.com/tests/typing")
text = driver.find_element(by=By.XPATH, value="//*[@id=\"root\"]/div/div[4]/div[1]/div/div[2]/div").text
pg.write(text)