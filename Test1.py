from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://trial-sport.ru/"
browser = webdriver.Chrome()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR, "#asc>div.line_bottom>div>div>input[type=text]")
search_string.send_keys("Сноуборд Bataleon GOLIATH 20Y WIDE")
button = browser.find_element(By.CSS_SELECTOR, "#srchFrm > div.search_line > div.search_submit > input[type=submit]").click()
time.sleep(3)
proverka = browser.find_element(By.CSS_SELECTOR, "#obj2840244 > span.txt > a > span").text
proverkaDA = "Сноуборд Bataleon GOLIATH 20Y WIDE"
if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()