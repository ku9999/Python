import time

# начальное состояние вентиляторов
fan1 = "Средне"
fan2 = "Стоп"
fan3 = "Максимум"

while True:
    # вывод текущего состояния вентиляторов
    print("Fan 1:", fan1)
    print("Fan 2:", fan2)
    print("Fan 3:", fan3)

    # задержка на 10 секунд
    time.sleep(10)

    # проверка текущего состояния и выбор действия
    if fan1 == "Средне" and fan2 == "Стоп" and fan3 == "Максимум":
        fan1 = "Максимум"
        fan2 = "Средне"
        fan3 = "Стоп"
    elif fan1 == "Максимум" and fan2 == "Средне" and fan3 == "Стоп":
        fan1 = "Стоп"
        fan2 = "Максимум"
        fan3 = "Средне"
    elif fan1 == "Стоп" and fan2 == "Максимум" and fan3 == "Средне":
        fan1 = "Средне"
        fan2 = "Стоп"
        fan3 = "Максимум"
    else:
        # если текущее состояние не соответствует ожидаемому,
        # включаем первый вентилятор на средней скорости,
        # а остальные выключаем
        fan1 = "Средне"
        fan2 = "Стоп"
        fan3 = "Стоп"
