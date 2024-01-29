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
button_enter = browser.find_element(By.CSS_SELECTOR, "#cm3").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#cm3_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(5) > p").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "#obj2896576 > span.txt > a.title > span").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div.main > div.wide_col > div.object_card > div.card_right > div.item_im_buy > div.item_im_buy__left > a.item_im_buy__but.js-show-buy-params").click()
button_enter = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div:nth-child(6) > div.popup.popup_buy_params > div.popup_win > div.popup_content > form > table:nth-child(6) > tbody > tr > td:nth-child(3) > div > div > input[type=submit]").click()
time.sleep(5)

proverka = browser.find_element(By.CSS_SELECTOR, "body > div.no_fix_header.body > div:nth-child(9) > div.popup.popup_buy > div.popup_win > div.c > div.popup-buy__title").text
proverkaDA = "Товар добавлен в корзину"

if proverka == proverkaDA:
   print("Тест прошел успешно")
else:
   print("Тест проверку не прошел")
browser.quit()



