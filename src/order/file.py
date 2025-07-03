try:
        choice = int(input("Введите целое число N: "))
        if choice <= 0:
            print("N должно быть положительным числом.")
        

        number_array = list(range(1, choice + 1))
        print("Массив чисел от 1 до", choice, ":", number_array)

        array_sum = sum(number_array)
        print("Сумма чисел в массиве:", array_sum)

except ValueError:
        print("Ошибка: Введите целое число.")

