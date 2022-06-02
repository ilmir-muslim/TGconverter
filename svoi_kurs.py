def svoi_kurs (svoykurs):
    summa = input('Введите сумму которую хотите обменять: ')
    result = float(svoykurs.replace(",", "."))*float(summa)
    print('результат = ' + str(result))
