DEFICIT_INDEX = 16.0
INSUFFICIENT_DEFICIT = 18.5
NORM = 25.0
EXCESS_MASS = 30.0
OBESITY_GRADE_1 = 35.0
OBESITY_GRADE_2 = 40.0
def calculate_bmi():
    try:
        weight = float(input("Введите ваш вес в килограммах: "))
        height = float(input("Введите ваш рост в метрах: например, 1.75 "))
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числовые значения.")
        return

    if height <= 0 or weight <= 0:
        print("Рост и вес должны быть положительными числами.")
        return

    bmi = weight / (height ** 2)
    bmi_rounded = round(bmi, 2)

    print(f"\nВаш индекс массы тела: {bmi_rounded}")

    if bmi < DEFICIT_INDEX:
        category = "Выраженный дефицит массы тела"
    elif DEFICIT_INDEX <= bmi <INSUFFICIENT_DEFICIT:
        category = "Недостаточная (дефицит) масса тела"
    elif INSUFFICIENT_DEFICIT <= bmi < NORM:
        category = "Норма"
    elif NORM <= bmi < EXCESS_MASS:
        category = "Избыточная масса тела (предожирение)"
    elif EXCESS_MASS <= bmi < OBESITY_GRADE_1:
        category = "Ожирение первой степени"
    elif OBESITY_GRADE_1 <= bmi < OBESITY_GRADE_2:
        category = "Ожирение второй степени"
    else:
        category = "Ожирение третьей степени"

    print(f"Категория: {category}")

if __name__ == "__main__":
    calculate_bmi()
