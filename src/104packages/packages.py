import calendar
import datetime
import time
from datetime import date

today = date.today()
year = today.year
month = today.month

print(calendar.month(year, month))

print('Сообщение появится через 5 секунд...')
time.sleep(5)
print('Это сообщение выведено с задержкой.')


def check_today_and_weekend():
    today = datetime.date.today()
    day_of_week = today.isoweekday()

    weekend_days = (6, 7)  # 6-суббота, 7-воскресенье

    if day_of_week in weekend_days:
        print(f'Сегодня {today.strftime("%d.%m.%Y")} - выходной день!')
    else:
        print(f'Сегодня {today.strftime("%d.%m.%Y")} - рабочий день.')


check_today_and_weekend()
