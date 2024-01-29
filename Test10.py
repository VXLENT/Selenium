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

#добавление в избранное
button_enter = browser.find_element(By.CSS_SELECTOR, "#cm4 > span").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#cm4_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(7) > p").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#notepad2840244").click()
time.sleep(5)

#вкладка избранное
button_enter = browser.find_element(By.CSS_SELECTOR, "#asc > div.line_top > div > div.head-user-buts > div > a.profile_lnk > span").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > noindex > div.left_col > div.page_tabs.b40 > a:nth-child(5)").click()

proverka = browser.find_element(By.CSS_SELECTOR, "#button_compare_all > div").text
proverkaDA = "сравнить выбранное"

if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
time.sleep(5)
browser.quit()



