from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://trial-sport.ru/"
browser = webdriver.Chrome()
browser.get(link)

registration_button = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
search_string = browser.find_element(By.CSS_SELECTOR, "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
search_string.send_keys("valentin-adarchenko@rambler.ru")
search_string = browser.find_element(By.CSS_SELECTOR, "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
search_string.send_keys("selenium12345")
button_enter = browser.find_element(By.CSS_SELECTOR, "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
time.sleep(3)

#Вход в корзину
button_enter = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.head-user-buts > a.cart_lnk > span").click()
#Удаление товара
button_enter = browser.find_element(By.CSS_SELECTOR, "#frm > table > tbody > tr.second-tr > td:nth-child(4) > div > span").click()
time.sleep(5)

proverka = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > noindex > div.right_col > div:nth-child(2) > div.b20").text
proverkaDA = "Корзина пуста. Вы можете вернуться в каталог и добавить товары к заказу."

if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()



