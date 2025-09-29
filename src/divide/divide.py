def divide_numbers():
    try:
        dividend = float(input('Введите число 1: '))
        divisor = float(input('Введите число 2: '))

        if divisor == 0:
            raise ZeroDivisionError('На ноль делить нельзя')

        return dividend / divisor

    except ZeroDivisionError as e:
        print(e)
        return None
    except ValueError:
        print('Ошибка: необходимо вводить только числа')
        return None


while True:
    result = divide_numbers()

    if result is not None:
        print(f'Результат деления: {result}')
        break
    else:
        print('Попробуйте снова.\n')
