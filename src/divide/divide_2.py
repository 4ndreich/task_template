REAL_AGE = 150


def get_age():
    while True:
        try:
            age = int(input('Введите ваш возраст: '))
            if age < 0:
                print('Возраст не может быть отрицательным!')
                continue
            if age > REAL_AGE:
                print('Введите реальный возраст!')
                continue
            return age
        except ValueError:
            print('Ошибка: введите целое число!')


print('Программа для определения возраста')
age = get_age()
print(f'Ваш возраст: {age} лет')
