import random

DIFF = 2


def random_number():
    secret_number = random.randint(0, 15)
    max_attempts = 3
    print('Загадано число от 0 до 15. Попробуйте угадать его за 3 попытки')

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f'Попытка {attempt}: Введите ваше число: '))
        except ValueError:
            print('Неверный ввод. Пожалуйста введите число')
            continue

        if guess == secret_number:
            print(f'Поздравляю! Вы угадали число {secret_number} c {attempt}-й попытки')
            return

        difference = abs(guess - secret_number)
        heat_level = 'тепло' if difference <= DIFF else 'холодно'
        direction = 'нужно больше' if guess < secret_number else 'нужно меньше'

        print(f'{heat_level}, {direction}!')
    print(f'К сожалению, вы не угадали. Загаданное число было: {secret_number}')


if __name__ == '__main__':
    random_number()
