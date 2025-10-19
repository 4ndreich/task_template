class CreditApplication:
    """Класс для обработки кредитной заявки."""

    # Константы для балльной системы
    AGE_THRESHOLD_1 = 21
    AGE_THRESHOLD_2 = 40
    INCOME_THRESHOLD_1 = 20000
    INCOME_THRESHOLD_2 = 40000
    AMOUNT_THRESHOLD_1 = 20000
    AMOUNT_THRESHOLD_2 = 40000
    SCORE_APPROVAL_THRESHOLD = 50

    # Баллы за различные критерии
    SCORE_AGE_YOUNG = 10
    SCORE_AGE_MATURE = 20
    SCORE_FEMALE = 10
    SCORE_INCOME_MEDIUM = 10
    SCORE_INCOME_HIGH = 20
    SCORE_CREDIT_HISTORY = 20
    SCORE_AMOUNT_LOW = 20
    SCORE_AMOUNT_MEDIUM = 10

    # Параметры кредита
    INTEREST_RATE = 0.05  # 5%
    LOAN_TERM_MONTHS = 12

    def __init__(self):
        self.fio = ''
        self.age = 0
        self.gender = ''
        self.income = 0.0
        self.has_credit_history = False
        self.requested_amount = 0.0
        self.score = 0

    def get_user_input(self):
        self.fio = input('Введите ФИО: ').strip()
        self.age = self._get_number_input('Введите возраст: ', int)
        self.gender = self._get_choice_input('Введите пол (м/ж): ', ['м', 'ж'])
        self.income = self._get_number_input('Введите доход в месяц: ', float)
        self.has_credit_history = self._get_choice_input(
            'Наличие кредитной истории (да/нет): ',
            ['да', 'д'],
        )
        self.requested_amount = self._get_number_input('Введите запрашиваемую сумму: ', float)

    def _get_number_input(self, prompt, data_type):
        while True:
            try:
                value = data_type(input(prompt))
                if value > 0:
                    return value
                print('Значение должно быть положительным.')
            except ValueError:
                print('Пожалуйста, введите число.')

    def _get_choice_input(self, prompt, valid_choices):
        """Ввод выбора из ограниченного набора вариантов."""
        while True:
            value = input(prompt).strip().lower()
            if value in valid_choices:
                return value in ['ж', 'да', 'д']
            print(f'Пожалуйста, введите один из: {", ".join(valid_choices)}')

    def calculate_score(self):
        # Возраст
        if self.age > self.AGE_THRESHOLD_2:
            self.score += self.SCORE_AGE_MATURE
        elif self.age >= self.AGE_THRESHOLD_1:
            self.score += self.SCORE_AGE_YOUNG

        # Пол
        if self.gender:
            self.score += self.SCORE_FEMALE

        # Доход
        if self.income > self.INCOME_THRESHOLD_2:
            self.score += self.SCORE_INCOME_HIGH
        elif self.income >= self.INCOME_THRESHOLD_1:
            self.score += self.SCORE_INCOME_MEDIUM

        # Кредитная история
        if self.has_credit_history:
            self.score += self.SCORE_CREDIT_HISTORY

        # Запрашиваемая сумма
        if self.requested_amount < self.AMOUNT_THRESHOLD_1:
            self.score += self.SCORE_AMOUNT_LOW
        elif self.requested_amount <= self.AMOUNT_THRESHOLD_2:
            self.score += self.SCORE_AMOUNT_MEDIUM

    def process_application(self):
        print('=== Кредитная заявка ===')
        self.get_user_input()
        self.calculate_score()

        print(f'\nФИО: {self.fio}')
        print(f'Набранные баллы: {self.score}')

        if self.score >= self.SCORE_APPROVAL_THRESHOLD:
            monthly_payment = self.requested_amount * (1 + self.INTEREST_RATE) / self.LOAN_TERM_MONTHS
            print('Решение: Кредит одобрен.')
            print(f'Ежемесячный платеж: {monthly_payment:.2f} руб.')
        else:
            print('Решение: В кредите отказано.')


if __name__ == '__main__':
    application = CreditApplication()
    application.process_application()
