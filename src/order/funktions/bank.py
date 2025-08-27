def bank(n, years):
    return n * (1.1 ** years)

def main():
    try:
        money = float(input("Сколько у вас денег для вклада? (рубли): "))
        years = int(input("На какой срок хотите сделать вклад? (лет): "))
        if money <= 0 or years <= 0:
            print("Ошибка: сумма и срок должны быть положительными числами.")
            return

        result = bank(money, years)
        
        print(f"Через {years} лет на вашем счету будет: {result:.2f} рублей")
    
    except ValueError:
        print("Ошибка: пожалуйста, вводите числовые значения.")
        
if __name__ == "__main__":
    main()    