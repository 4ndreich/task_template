base = {}
print ("Добро пожаловать в наше приложение")
while True:
    choice = input("Введите 1, чтобы зарегистрироваться \nВведите 2, чтобы авторизоваться \nВведите 3, чтобы выйти из программы \nВведите 4,чтобы сменить пароль пользователя \n") 
    print(base)
    if choice == "1":
        print("Процесс регистристрации")
        login = input("Введите логин: \n")
        if login in base:
            print("Такой логин уже существует")
            continue
        if '#' in login:
         print("Ошибка: Логин не должен содержать символ '#'")
        
        password = input ("Введите пароль: \n")
        if password == "":
            print("Пароль не может быть пустой строкой")
            continue

        password_again = input("Введите пароль повторно: \n")
        if password == password_again:
            base[login] = password
            print("Процесс регистрации завершен успешно")
        elif password != password_again:
            print("Пароли не совпадают")
            continue
        else:
            print("Error!!!")
            break
        login = input("Введите логин: \n")
        attempts = 0
        if login in base:
            print("Такой существует")
            password = input ("Введите пароль: \n")
            if password == base[login]:
                print("Вы успешно вошли в систему")
                break
            while attempts < 3:
                attempts += 1
                print("Пароль неверный")
                print("Попробуйте ещё раз")
                password = input("Введите пароль: \n")
                if password == base[login]:
                    print("Вы успешно вошли в систему")
                    print(base)
                    break
            print("Пароль неверный")
            print("Пройдите авторизацию заново")
            break
        else:
            print("Такой пользователь не зарегистрирован")
            continue
     
    elif choice == "4":
        print("Смена пароля")
        login = input("Введите ваш логин: \n")
        if login in base:
            password = input("Введите ваш пароль: \n")
            if password == base[login]:
                print(base)
                print("Смена пароля")
                print("Введите ваш новый пароль")
                new_password = input()
                base[login] = new_password
                print(base)
                continue
            else:
                print("Пароль неверный")
                continue
        else:
            print("Логин не найден")
            continue
    else:
        print("Выход из программы")
        break
import uuid
def generate_unique_id():
  return uuid.uuid4()
user_id = generate_unique_id()
print(f"Уникальный ID пользователя: {user_id}")


    
