class MedicalRecord:
    def __init__(self, full_name, gender, birth_date, address, diseases=None):
        self.full_name = full_name
        self.gender = gender
        self.birth_date = birth_date
        self.address = address
        self.diseases = diseases if diseases is not None else []

    def display_info(self):
        print(f'ФИО: {self.full_name}')
        print(f'Пол: {self.gender}')
        print(f'Дата рождения: {self.birth_date}')
        print(f'Адрес: {self.address}')
        print(f'Заболевания: {", ".join(self.diseases) if self.diseases else "нет заболеваний"}')
        print('-' * 50)


if __name__ == '__main__':
    medical_records = [
        MedicalRecord(
            'Иванов Иван Иванович',
            'Мужской',
            '15.03.1985',
            'г. Москва, ул. Ленина, д. 15, кв. 34',
            ['Гипертония', 'Сахарный диабет 2 типа'],
        ),
        MedicalRecord(
            'Петрова Мария Сергеевна',
            'Женский',
            '22.07.1990',
            'г. Санкт-Петербург, ул. Пушкина, д. 8, кв. 12',
            ['Бронхиальная астма'],
        ),
        MedicalRecord(
            'Сидоров Алексей Петрович',
            'Мужской',
            '03.11.1978',
            'г. Екатеринбург, ул. Мира, д. 45, кв. 67',
            ['Гастрит', 'Остеохондроз'],
        ),
        MedicalRecord(
            'Козлова Анна Владимировна',
            'Женский',
            '18.05.1995',
            'г. Новосибирск, ул. Советская, д. 23, кв. 9',
            ['Мигрень'],
        ),
        MedicalRecord(
            'Федоров Дмитрий Николаевич',
            'Мужской',
            '30.09.1982',
            'г. Казань, ул. Гагарина, д. 12, кв. 15',
            [],
        ),
    ]

    for record in medical_records:
        record.display_info()
