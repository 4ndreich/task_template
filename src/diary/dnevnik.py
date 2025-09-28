import sys

MIN_YEAR = 1900
MAX_YEAR = 2100
MIN_DAY = 1
MAX_DAY = 31
MIN_MONTH = 1
MAX_MONTH = 12
DAY_STRING_LENGTH = 2
MONTH_STRING_LENGTH = 2
YEAR_STRING_LENGTH = 4


def get_date():
    while True:
        date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
        if validate_date(date):
            return date
        print('Неверный формат даты! Попробуйте еще раз')


def validate_date(date):
    try:
        day, month, year = date.split('.')
        if len(day) != DAY_STRING_LENGTH or len(month) != MONTH_STRING_LENGTH or len(year) != YEAR_STRING_LENGTH:
            return False

        day_int = int(day)
        month_int = int(month)
        year_int = int(year)

        return (
            MIN_MONTH <= month_int <= MAX_MONTH and MIN_DAY <= day_int <= MAX_DAY and MIN_YEAR <= year_int <= MAX_YEAR
        )

    except (ValueError, TypeError):
        return False


def get_message():
    print('Введите запись в дневник (для завершения введите пустую строку):')
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return '\n'.join(lines)


def save_entry(date, message):
    """Функция для сохранения записи в файл"""
    with open('diary.txt', 'a', encoding='utf-8') as file:
        file.write(f'{date}\n{message}\n\n')


def main():
    print('=== ДНЕВНИК ===')
    print('Добро пожаловать в ваш дневник!')

    while True:
        print('\n1. Сделать новую запись')
        print('2. Выйти из программы')

        choice = input('Выберите действие: ')

        if choice == '1':
            date = get_date()
            message = get_message()
            save_entry(date, message)
            print('Запись успешно сохранена!')
        elif choice == '2':
            print('До свидания! Ваши записи сохранены в файле diary.txt')
            sys.exit()
        else:
            print('Неверный выбор! Попробуйте еще раз.')


if __name__ == '__main__':
    main()
