import sys
from datetime import datetime

MIN_YEAR = 1900
MAX_YEAR = 2100


def validate_date(date):
    try:
        date_obj = datetime.strptime(date, "%d.%m.%Y")
        return MIN_YEAR <= date_obj.year <= MAX_YEAR
    except ValueError:
        return False


def get_date():
    while True:
        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
        if validate_date(date):
            return date
        print("Неверный формат даты! Попробуйте еще раз")


def get_message():
    print("Введите запись в дневник (для завершения введите пустую строку):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def save_entry(date, message):
    """Функция для сохранения записи в файл"""
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"{date}\n{message}\n\n")


def main():
    print("=== ДНЕВНИК ===")
    print("Добро пожаловать в ваш дневник!")

    while True:
        print("\n1. Сделать новую запись")
        print("2. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            date = get_date()
            message = get_message()
            save_entry(date, message)
            print("Запись успешно сохранена!")
        elif choice == "2":
            print("До свидания! Ваши записи сохранены в файле diary.txt")
            sys.exit()
        else:
            print("Неверный выбор! Попробуйте еще раз.")


if __name__ == "__main__":
    main()
