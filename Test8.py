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

#смена города
button_enter = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.city_wrap > div > span:nth-child(1)").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body.index > div:nth-child(11) > div.city_popup.city_popup_new > div.c > div > div > div.jspPane > div > div.cities > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > a > span").click()
time.sleep(5)

proverka = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.city_wrap > div > span:nth-child(1)").text
proverkaDA = "Москва"

if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()



