class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.94,
            'RUB': 90.0,
        }

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.exchange_rates:
            raise ValueError(f'Неизвестная валюта: {from_currency}')

        if to_currency not in self.exchange_rates:
            raise ValueError(f'Неизвестная валюта: {to_currency}')
        # возращаем конвертацию через USD
        return (amount / self.exchange_rates[from_currency]) * self.exchange_rates[to_currency]

    def get_available_currencies(self):
        return list(self.exchange_rates.keys())

    def info_conversion(self):
        print('Добро пожаловать в конвертер валют!')
        print('Доступные валюты:', ', '.join(self.get_available_currencies()))
        print()

        # Выбираем валюту для покупки
        print('Какую валюту вы хотите купить?')
        to_currency = input('Введите код валюты (USD, EUR, RUB): ').upper()

        if to_currency not in self.exchange_rates:
            print('Ошибка: Неизвестная валюта!')

        # Выбираем валюту, которой располагает пользователь
        print('\nКакой валютой вы располагаете?')
        from_currency = input('Введите код валюты (USD, EUR, RUB): ').upper()

        if from_currency not in self.exchange_rates:
            print('Ошибка: Неизвестная валюта!')
            return

        # Ввод суммы для конвертации
        try:
            amount = float(input(f'\nСколько {to_currency} вы хотите купить? '))
        except ValueError:
            print('Ошибка: Введите корректное число!')
            return

        #  конвертация
        try:
            result = self.convert(amount, to_currency, from_currency)

            # итог
            print('\n' + '=' * 50)
            print('РЕЗУЛЬТАТЫ КОНВЕРТАЦИИ:')
            print(f'Вы хотите купить: {amount:.2f} {to_currency}')
            print(f'Для этого вам нужно: {result:.2f} {from_currency}')
            print(f'Курс обмена: 1 {to_currency} = {result / amount:.2f} {from_currency}')
            print('=' * 50)

        except Exception as e:
            print(f'Ошибка при конвертации: {e}')


if __name__ == '__main__':
    converter = CurrencyConverter()
    converter.info_conversion()
