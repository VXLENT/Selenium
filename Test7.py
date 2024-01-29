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

#добавление к сравнению
button_enter = browser.find_element(By.CSS_SELECTOR, "#cm4 > span").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#cm4_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(7) > p").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#compare2840244").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#compare2840375").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#compare2837285").click()

#Очистка сравнений
button_enter = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.head-user-buts > a.compare_lnk > span").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > div.wide_col > div.compare__tabs.loaded > div:nth-child(2) > span").click()
time.sleep(5)

proverka = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > div.wide_col > p:nth-child(1)").text
proverkaDA = "Не выбрано ни одного товара для сравнения."

if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()



