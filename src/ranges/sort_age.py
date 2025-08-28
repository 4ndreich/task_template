MAX_KIDS_AGE = 12
MAX_TEENAGERS_AGE = 18
MAX_CLUB27_AGE = 27
MAX_YOUNG_AGE = 45
MAX_MATURE_AGE = 60
MAX_ELDERLY_AGE = 74
MAX_YOUNG_AT_HEART = 90

print("Введите ваш возраст")
while True:
    age = input()
    if not age.isdigit():
        print("Введите целое число")
    else:
        age = int(age)
        break
if age <= MAX_KIDS_AGE:
    print("От 0 до 12 - дети")
elif age <= MAX_TEENAGERS_AGE:
    print("От 12 до 18 - подростки")
elif age <= MAX_CLUB27_AGE:
    print("От 18 до 27 - клуб 27")
elif age <= MAX_YOUNG_AGE:
    print("От 27 до 45 - молодые")
elif age <= MAX_MATURE_AGE:
    print("От 45 до 60 - зрелые")
elif age <= MAX_ELDERLY_AGE:
    print("От 60 до 74 - пожилые")
elif age <= MAX_YOUNG_AT_HEART:
    print("От 74 до 90 - молоды в душе")
else:
    print("От 90 и выше - долгожители")
