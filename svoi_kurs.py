def svoi_kurs (svoykurs):
    summa = input('Введите сумму которую хотите обменять: ')
    result = float(svoykurs.replace(",", "."))*float(summa)
    result = round(result, 2)
    print('результат = ' + str(result))
