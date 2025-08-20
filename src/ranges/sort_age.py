print("Введите ваш возраст")
while True:
    age = input()
    if not age.isdigit():
        print("Введите целое число")
    else:
        age = int(age)
        break
if age <= 12:
    print("От 0 до 12 - дети")
elif age <= 18:
    print("От 12 до 18 - подростки")
elif age <= 27:
    print("От 18 до 27 - клуб 27")
elif age <= 45:
    print("От 27 до 45 - молодые")
elif age <= 60:
    print("От 45 до 60 - зрелые")
elif age <= 74:
    print("От 60 до 74 - пожилые")
elif age <= 90:
    print("От 74 до 90 - молоды в душе")
else:
    print("От 90 и выше - долгожители")
