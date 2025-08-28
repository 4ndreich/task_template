DIFFERENCE = 0.01
def main():
    try:
        dollars =float(input("Введите  количество долларов:"))
        rubles = float(input("Введите количество рублей:"))
        rate = float(input("Введите текущий курс доллара в рублях:"))
    except ValueError:
        print("Ошибка ввода. Введите числовые значения.")
        return

    total_rub = dollars * rate + rubles

    target_rub = total_rub / 2
    target_dollar = total_rub / (2 * rate)

    rub_diff = rubles - target_rub
    dollar_diff = dollars - target_dollar

    if abs(rub_diff) < DIFFERENCE:
        print("Портфель уже сбалансирован.")
    elif rub_diff > 0:
        # Продаём излишек рублей для покупки долларов
        exchange_rub = round(rub_diff, 2)
        exchange_dollars = round(exchange_rub / rate, 2)
        print(f"Продайте {exchange_rub:.2f} рублей для покупки {exchange_dollars:.2f} долларов.")
    else:
        # Продаём излишек долларов для покупки рублей !
        exchange_dollars = round(-dollar_diff, 2)
        exchange_rub = round(exchange_dollars * rate, 2)
        print(f"Продайте {exchange_dollars:.2f} долларов для покупки {exchange_rub:.2f} рублей.")

if __name__ == "__main__":
    main()
