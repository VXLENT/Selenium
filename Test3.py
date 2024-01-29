from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://trial-sport.ru/"
browser = webdriver.Chrome()
browser.get(link)
#Проверка перехода на страницу акций

button = browser.find_element(By.CSS_SELECTOR, "#item2 > span").click()
time.sleep(3)
stock = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > div.wide_col > div.acts > div:nth-child(1) > a").click()
proverka = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > div.navigation.b20 > div.page-head > div.page-title > h1").text
proverkaDA = "Акции и скидки"
if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()