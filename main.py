import USD_RUB as fl1
import EGP_RUB as fl2
import svoi_kurs as fl3
# Импортируем файлы содержащие соответствующие функции

def callfunc (call):
    if call == '1':
        fl1.currency = fl1.USD_RUB_Currency() # Создание объекта и вызов метода
        fl1.currency.check_currency()
    elif call == '2':
        fl2.currency = fl2.EGP_RUB_Currency()
        fl2.currency.check_currency()
    elif call == '3':
        fl3.svoi_kurs(input('Введите свой курс: '))

callfunc(input('введите 1, если доллары в рубли, 2 если гинеи в рубли или 3 если меняем по своему курсу: '))