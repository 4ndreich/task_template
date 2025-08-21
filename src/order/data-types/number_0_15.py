import random
def random_number():
    secret_number = random.randint(0,15)
    max_attempts = 3
    print("Загадано число от 0 до 15. Попробуйте угадать его за 3 попытки")
    for attempts in range(1,max_attempts +1):
        try:
            guess = int(input(f"Попытка {attempts}: Введите ваше число:"))
        except ValueError:
            print("Неверный ввод. Пожалуйста введите число")
            continue
        if guess == secret_number:
            print(f"Поздравляю!. Вы угадали число {secret_number} c {attempts}-й попытки")
            return
        difference = abs(guess -secret_number)
        if difference <= 2:
            heat_level = "тепло"
        else:
            heat_level = "холодно"
        if guess < secret_number:
            direction = "нужно больше"
        else:
            direction = "нужно меньше"
        print(f"{heat_level},{direction}!")
random_number()
