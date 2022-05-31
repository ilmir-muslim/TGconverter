import requests #модуль для обработки URL
from bs4 import BeautifulSoup #Модуль для работы с HTML
import time # Модуль для остановки программы
#import telebot # посмотреть какой модуль лучше подключить для работы с ботом, переделать код для телеграмм бота

#модель для конвертации гиней в рубли

# Основной класс
class EGP_RUB_Currency:
    #Ссылка на нужную страницу
    EGP_RUB = 'https://www.google.com/search?q=1+%D0%B5%D0%B3%D0%B8%D0%BF%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D1%84%D1%83%D0%BD%D1%82+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D1%8F%D1%85&sxsrf=ALiCzsZhwKZMZ9FTuaTnw5HCt_dHsijRvA%3A1654005278403&ei=Hh6WYpuVGMT3kgXO2ISgBQ&oq=1+%D0%B5%D0%B3%D0%B8%D0%BF%D0%B5+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D1%8F%D1%85&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQHhAHMgYIABAeEAcyCggAEB4QDxAIEAcyCggAEB4QDxAIEAc6BwgAEEcQsAM6BAgAEA06CAgAEB4QCBANSgQIQRgASgQIRhgAUKwgWPAlYLkvaANwAXgAgAGHBIgB3g2SAQkyLTIuMS4xLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
    #Заголовки для передачи  вместе с URL
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    current_converted_price = 0
 #   difference = 5 #Разница после которой будет отправлено сообщение на почту

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    # Метод для получения курса валюты
    def get_currency_price(self):
        full_page = requests.get(self.EGP_RUB, headers=self.header)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')
        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text
    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        vibor = input('менять по курсу (введите: 1), с наценкой (введите: 2) или использовать свой курс (Веедите 3): ')
        if vibor == '1':
            summa = input('Введите сумму которую хотите обменять: ')
            result = currency * float(summa)

        elif vibor == '2':
            procent = input("введите процент наценки: ")
            summa = input('Введите сумму которую хотите обменять: ')
            result = (currency + currency * (float(procent) / 100)) * float(summa)

        elif vibor == '3':
            svoykurs = input('Введите свой курс: ')
            summa = input('Введите сумму которую хотите обменять: ')
            result = float(svoykurs.replace(",", "."))*float(summa)

        else:
            print('вы сделали не правильный выбор :(')

        print('результат = ' + str(result))


# Создание объекта и вызов метода
currency = EGP_RUB_Currency()
currency.check_currency()
#дальше выносим функию с выбором с отдельный файл (позднее это будет файл диалога с ботом)