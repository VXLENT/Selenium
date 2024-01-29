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
proverka = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.head-user-buts > div > a.profile_lnk > span").text
proverkaDA = "Личный кабинет"
if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()



