import pickle
import time
import urllib
import requests
import shutil
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import re
import urllib.request
from googletrans import Translator
import translators


# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Driver startup

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_options)


def banners():
    while 1:
        try:
            driver.find_element_by_xpath(
                '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div[1]/form/button').click()
        except NoSuchElementException:
            break


def login():
    # Admin Panel login
    driver.get('https://autoshina.md/')
    while True:
        try:
            driver.find_element_by_xpath(
                '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').send_keys(
                'login')
            password = driver.find_element_by_xpath(
                '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input').send_keys(
                'password')
            captcha = driver.find_element_by_xpath(
                '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input').send_keys(
                input('Введите капчу: '))
            enter = driver.find_element_by_class_name('form_btn').click()
            mainPage = driver.current_window_handle

        except NoSuchElementException:
            pass
        break


login()


for page in range(1, 5):
    for tr in range(2, 51):
        banners()
        driver.get('https://autoshina.md/alfabetaomegason73naasfalteon/iblock/catalog_brands/catalog_brands_models/list_elem.php?id=2&page={}'.format(page))
        banners()
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr[{}]/td[4]/a[1]'.format(tr)).click()
        driver.find_element_by_xpath('//*[@id="item_description"]/ul/li[3]/a').click()
        l = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div').text
        link = l.replace(' ', '-').replace('+', '').lower()
        # if '4x4' in link: link += '-'
        driver.get('https://autoshina.md/' + link)

        time.sleep(2.5)
        try:
            driver.find_element_by_xpath('//*[@id="page"]/div[4]/div[1]/div[2]').click()
        except NoSuchElementException:
            print(link)
            driver.get('https://autoshina.md/' + link[:-1] + '/new/')
            time.sleep(2.5)
            driver.find_element_by_xpath('//*[@id="page"]/div[4]/div[1]/div[2]').click()


        char1 = driver.find_element_by_xpath('//*[@id="page"]/div[5]/div[2]/div[3]/div/div[1]/div/div[3]/p').text
        char2 = driver.find_element_by_xpath('//*[@id="page"]/div[5]/div[2]/div[3]/div/div[2]/div/div[3]/p').text
        char3 = driver.find_element_by_xpath('//*[@id="page"]/div[5]/div[2]/div[3]/div/div[3]/div/div[3]/p').text

        # print(char1, char2, char3, end='\n')
        driver.back()
        driver.back()


        # driver.get('https://autoshina.md/alfabetaomegason73naasfalteon/iblock/catalog_brands/catalog_brands_models/list_elem.php?id=2&page={}'.format(page))
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr[{}]/td[4]/a[2]'.format(tr)).click()
        error = ''
        try:
            driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[4]/a').click()
        except NoSuchElementException:
            error = 'error'
            print('Пустая модель!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div[1]/a').click()
        # Заливаем картинки

        # Char 1
        if error:
            pass
        else:
            if 'рисунок' in char1 or 'рисунка' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Ассиметричный_рисунок_протектора.jpg')
            elif 'резиновой смеси' in char1 or 'резиновая смесь' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Резиновая_смесь.jpg')
            elif 'Twaron' in char1 or 'TWARON' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Twaron.jpg')
            elif 'Dynamic Response' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Dynamic_Response.jpg')
            elif 'арамидно-нейлоновый слой' in char1 or 'арамидно-нейлонового слоя' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Арамидно-нейлоновый_слой_и_резиновая_смесь.jpg')
            elif 'пятно контакта' in char1 or 'пятна контакта' in char1 or 'пятне контакта' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Пятно_контакта.png')
            elif 'спортивный дизайн' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Спортивный_дизайн.jpg')
            elif 'акустический комфорт' in char1 or 'уровень шума' in char1 or 'уровня шума' in char1 or 'шумов' in char1 or 'шумы' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Акустический_комфорт.jpg')
            elif 'износ' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Износ_шины.jpg')
            elif 'мокр' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Аквапланирование.jpg')
            elif 'ламели' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Ламели.png')
            elif 'брекерный' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Дополнительный_брекерный_слой.png')
            elif 'экологи' in char1 or 'расход' in char1 or 'выбросов' in char1 or 'выброса' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Экология.jpg')
            elif 'сцепление' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Сцепление.jpg')
            elif 'индикатор' in char1 and 'износ' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Индикатор износа.jpg')
            elif 'внезапно' in char1:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/allseason.jpg')
            else:
                print('Нет характеристики #1')
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[3]/div[2]/input').send_keys('D://char/Бибендум_1.jpg')

            # Char 2
            if 'рисунок' in char2 or 'рисунка' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Ассиметричный_рисунок_протектора.jpg')
            elif 'резиновой смеси' in char2 or 'резиновая смесь' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Резиновая_смесь_2.jpg')
            elif 'Twaron' in char2 or 'TWARON' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Twaron.jpg')
            elif 'Dynamic Response' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Dynamic_Response.jpg')
            elif 'Арамидно-нейлоновый слой' in char2 or 'арамидно-нейлонового слоя' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Арамидно-нейлоновый_слой_и_резиновая_смесь.jpg')
            elif 'пятно контакта' in char2 or 'пятна контакта' in char2 or 'пятне контакта' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Пятно_контакта.png')
            elif 'спортивный дизайн' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Спортивный_дизайн.jpg')
            elif 'акустический комфорт' in char2 or 'уровень шума' in char2 or 'уровня шума' in char2 or 'шумов' in char2 or 'шумы' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Акустический_комфорт.jpg')
            elif 'износ' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Износ_шины.jpg')
            elif 'мокр' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Аквапланирование.jpg')
            elif 'ламели' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Ламели_2.jpg')
            elif 'брекерный' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Дополнительный_брекерный_слой.png')
            elif 'экологи' in char2 or 'расход' in char2 or 'выбросов' in char2 or 'выброса' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Экология.jpg')
            # elif 'сцепление' in char2 or 'снег' in char2:
            #     driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Сцепление_с_дорогой_(Зима)_2.jpg')
            elif 'сцепление' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Сцепление.jpg')

            elif 'индикатор' in char2 and 'износ' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Индикатор износа.png')
            elif 'внезапно' in char2:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/allseason.jpg')
            else:
                print('Нет характеристики #2')
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[5]/div[2]/input').send_keys('D://char/Бибендум_2.png')

            # Char 3
            if 'рисунок' in char3 or 'рисунка' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Ассиметричный_рисунок_протектора.jpg')
            elif 'резиновой смеси' in char3 or 'резиновая смесь' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Резиновая_смесь_2.jpg')
            elif 'Twaron' in char3 or 'TWARON' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Twaron.jpg')
            elif 'Dynamic Response' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Dynamic_Response.jpg')
            elif 'Арамидно-нейлоновый слой' in char3 or 'арамидно-нейлонового слоя' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Арамидно-нейлоновый_слой_и_резиновая_смесь.jpg')
            elif 'пятно контакта' in char3 or 'пятна контакта' in char3 or 'пятне контакта' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Пятно_контакта.png')
            elif 'спортивный дизайн' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Спортивный_дизайн.jpg')
            elif 'акустический комфорт' in char3 or 'уровень шума' in char3 or 'уровня шума' in char3 or 'шумов' in char3 or 'шумы' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Акустический_комфорт.jpg')
            elif 'износ' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Аквапланирование.jpg')
            elif 'ламели' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Ламели_3.jpg')
            elif 'брекерный' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Дополнительный_брекерный_слой.png')
            elif 'экологи' in char3 or 'расход' in char3 or 'выбросов' in char3 or 'выброса' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Экология.jpg')
            # elif 'сцепление' in char3 or 'снег' in char3:
            #     driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Сцепление_с_дорогой_(Зима)_1.jpg')
            elif 'сцепление' in char1 or 'снег' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Сцепление.jpg')
            elif 'индикатор' in char3 and 'износ' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Индик износа.jpg')
            elif 'внезапно' in char3:
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/allseason.jpg')
            else:
                print('Нет характеристики #3')
                driver.find_element_by_xpath('//*[@id="item_description"]/div[1]/div[7]/div[2]/input').send_keys('D://char/Бибендум_3.png')

            print(l)
            print('__________________________________________')
            driver.find_element_by_xpath('//*[@id="ok"]').click()
            driver.find_element_by_xpath('//*[@id="item_description"]/ul/li[1]/a').click()
            # driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a').click()
            # driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div[15]/a').click()
            # driver.find_element_by_xpath('//*[@id="item_description"]/ul/li/a').click()