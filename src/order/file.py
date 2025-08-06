def get_initials():
  surname = input("Введите фамилию: ")
  name = input("Введите имя: ")
  patronymic = input("Введите отчество: ")
  initials = f"{surname} {name[0]}.{patronymic[0]}."
  print(initials)
get_initials("Ваше имя сокращенное")
