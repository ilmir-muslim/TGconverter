import requests #модуль для обработки URL
from bs4 import BeautifulSoup #Модуль для работы с HTML
import time # Модуль для остановки программы
#import telebot # посмотреть какой модуль лучше подключить для работы с ботом, переделать код для телеграмм бота

# СЛЕДУЮЩИЙ ШАГ СОЕДЕНИТЬ ЭТОД КОД С КОДОМ БОТА КОНВЕРТЕРА!

# Основной класс
class Currency:
    #Ссылка на нужную страницу
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    #Заголовки для передачи  вместе с URL
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    current_converted_price = 0
 #   difference = 5 #Разница после которой будет отправлено сообщение на почту

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    # Метод для получения курса валюты
    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.header)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')
        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text
    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        vibor = input('менять по курсу (введите: 1) или с наценкой (введите: 2): ')
        if vibor == '1':
            print('курс доллара к рублю: ' + str(currency))
        elif vibor == '2':
            procent = input("введите процент наценки: ")
            svoikurs = currency + currency * (float(procent)/100)
            print('курс с наценкой: ' + str(svoikurs))
        else:
            print('вы сделали не правильный выбор :(')



# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()
