def vowels():
    text = input("Введите слово: ")
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for letter in text:
        if letter in vowels:
         count += 1   
    print(f"Количество гласных в слове '{text}': {count}")
vowels()