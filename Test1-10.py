import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class AdarchenkoTest(unittest.TestCase):
    def test_1(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        # Проверка поиска
        search_string = browser.find_element(By.CSS_SELECTOR, "#asc>div.line_bottom>div>div>input[type=text]")
        search_string.send_keys("Сноуборд Bataleon GOLIATH 20Y WIDE")
        button = browser.find_element(By.CSS_SELECTOR,
                                      "#srchFrm > div.search_line > div.search_submit > input[type=submit]").click()
        time.sleep(3)
        proverka = browser.find_element(By.CSS_SELECTOR, "#obj2840244 > span.txt > a > span").text
        proverkaDA = "Сноуборд Bataleon GOLIATH 20Y WIDE"
        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_2(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        # Регистрация
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        button_enter = browser.find_element(By.CSS_SELECTOR,
                                            "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)
        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "#asc > div.line_top > div > div.head-user-buts > div > a.profile_lnk > span").text
        proverkaDA = "Личный кабинет"
        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_3(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        # Проверка перехода на страницу акций
        browser.find_element(By.CSS_SELECTOR, "#item2 > span").click()
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body > div.main > div.wide_col > div.acts > div:nth-child(1) > a").click()
        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "body > div.no_fix_header.body > div.main > div.navigation.b20 > div.page-head > div.page-title > h1").text
        proverkaDA = "Акции и скидки"
        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_4(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        # Проверка добавления товара в корзину
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "#cm3").click()
        browser.find_element(By.CSS_SELECTOR,
                             "#cm3_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(5) > p").click()
        browser.find_element(By.CSS_SELECTOR, "#obj2896576 > span.txt > a.title > span").click()
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body > div.main > div.wide_col > div.object_card > div.card_right > div.item_im_buy > div.item_im_buy__left > a.item_im_buy__but.js-show-buy-params").click()
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body > div:nth-child(6) > div.popup.popup_buy_params > div.popup_win > div.popup_content > form > table:nth-child(6) > tbody > tr > td:nth-child(3) > div > div > input[type=submit]").click()
        time.sleep(5)

        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "body > div.no_fix_header.body > div:nth-child(9) > div.popup.popup_buy > div.popup_win > div.c > div.popup-buy__title").text
        proverkaDA = "Товар добавлен в корзину"

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_5(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)

        # Вход в корзину
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > a.cart_lnk > span").click()
        # Удаление товара
        browser.find_element(By.CSS_SELECTOR,
                             "#frm > table > tbody > tr.second-tr > td:nth-child(4) > div > span").click()
        time.sleep(5)

        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "body > div.no_fix_header.body > div.main > noindex > div.left_col > div.page_tabs.b40 > a.active > span > b").text
        proverkaDA = "0"

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_6(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)

        # добавление к сравнению
        browser.find_element(By.CSS_SELECTOR, "#cm4 > span").click()
        browser.find_element(By.CSS_SELECTOR,
                             "#cm4_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(7) > p").click()
        browser.find_element(By.CSS_SELECTOR, "#compare2840244").click()
        browser.find_element(By.CSS_SELECTOR, "#compare2840375").click()
        browser.find_element(By.CSS_SELECTOR, "#compare2837285").click()
        time.sleep(5)

        # Переход в сравнение
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > a.compare_lnk > span").click()

        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "body > div.no_fix_header.body > div.main > div.wide_col > div.compare__tabs.loaded > div:nth-child(2) > span").text
        proverkaDA = "очистить в категории"

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_7(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)

        # добавление к сравнению
        browser.find_element(By.CSS_SELECTOR, "#cm4 > span").click()
        browser.find_element(By.CSS_SELECTOR,
                             "#cm4_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(7) > p").click()
        browser.find_element(By.CSS_SELECTOR, "#compare2840244").click()
        browser.find_element(By.CSS_SELECTOR, "#compare2840375").click()
        browser.find_element(By.CSS_SELECTOR, "#compare2837285").click()

        # Очистка сравнений
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > a.compare_lnk > span").click()
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body > div.main > div.wide_col > div.compare__tabs.loaded > div:nth-child(2) > span").click()
        time.sleep(5)

        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "body > div.no_fix_header.body > div.main > div.wide_col > p:nth-child(1)").text
        proverkaDA = "Не выбрано ни одного товара для сравнения."

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_8(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)

        # смена города
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.city_wrap > div > span:nth-child(1)").click()
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body.index > div:nth-child(11) > div.city_popup.city_popup_new > div.c > div > div > div.jspPane > div > div.cities > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > a > span").click()
        time.sleep(5)

        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "#asc > div.line_top > div > div.city_wrap > div > span:nth-child(1)").text
        proverkaDA = "Москва"

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_9(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)

        # выбор магазина
        browser.find_element(By.CSS_SELECTOR, "#item5 > span").click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body > div.big_map_wrap > div.layer.big_map_shops > div.scroll > div > div > div > div > div.item.shop.visible.first > div:nth-child(1) > div").click()
        time.sleep(5)

        proverka = browser.find_element(By.CSS_SELECTOR,
                                        "body > div.no_fix_header.body > div.big_map_wrap > div.layer.big_map_shop > div.scroll.jspScrollable > div > div.jspPane > div > div.item.shop > div:nth-child(1) > div").text
        proverkaDA = "ул. Мужества, д. 10, ТЦ \"Зеленый\""

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        browser.quit()
        pass

    def test_10(self):
        link = "https://trial-sport.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > span > span").click()
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > input[type=text]")
        search_string.send_keys("valentin-adarchenko@rambler.ru")
        search_string = browser.find_element(By.CSS_SELECTOR,
                                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > input[type=password]")
        search_string.send_keys("selenium12345")
        browser.find_element(By.CSS_SELECTOR,
                             "#idLogForm > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > input[type=submit]").click()
        time.sleep(3)

        # добавление в избранное
        browser.find_element(By.CSS_SELECTOR, "#cm4 > span").click()
        browser.find_element(By.CSS_SELECTOR,
                             "#cm4_sub > div > div > div > div.jspPane > div > div:nth-child(1) > a:nth-child(7) > p").click()
        browser.find_element(By.CSS_SELECTOR, "#notepad2840244").click()
        time.sleep(5)

        # вкладка избранное
        browser.find_element(By.CSS_SELECTOR,
                             "#asc > div.line_top > div > div.head-user-buts > div > a.profile_lnk > span").click()
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.no_fix_header.body > div.main > noindex > div.left_col > div.page_tabs.b40 > a:nth-child(5)").click()

        proverka = browser.find_element(By.CSS_SELECTOR, "#button_compare_all > div").text
        proverkaDA = "сравнить выбранное"

        if proverka == proverkaDA:
            print("Тест прошел успешно")
        else:
            print("Тест проверку не прошел")
        time.sleep(5)
        browser.quit()
        pass
