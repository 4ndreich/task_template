shop = {
    'молочное': {
        'молоко': 100,
    },
    'мучное': {
        'хлеб': 200,
    },
}

basket = {}  # Корзина пользователя
feedbacks = []  # Список для хранения отзывов


def add_products(user_group, **products):
    if user_group in shop:
        shop[user_group].update(products)
        print(f"Товары добавлены в раздел '{user_group}'")
    else:
        shop[user_group] = products
        print(f"Создан новый раздел '{user_group}' с товарами")
    return shop


def remove_product(group_name, product_name):
    if group_name in shop:
        if product_name in shop[group_name]:
            del shop[group_name][product_name]
            print(f"Товар '{product_name}' удален из раздела '{group_name}'")
            return True
        print(f"Ошибка: Товар '{product_name}' не найден в разделе '{group_name}'")
        return False
    print(f"Ошибка: Раздел '{group_name}' не найден")
    return False


def print_all_products():
    if not shop:
        print('Магазин пуст!')
        return
    print('\n' + '=' * 40)
    print('ВСЕ ТОВАРЫ В МАГАЗИНЕ:')
    print('=' * 40)
    for group, products in shop.items():
        print(f'\nРАЗДЕЛ: {group.upper()}')
        if products:
            for product, price in products.items():
                print(f'  - {product}: {price} руб.')
        else:
            print('  (товары отсутствуют)')
    print('=' * 40 + '\n')


def print_group_products(group_name):
    if group_name not in shop:
        print(f"Ошибка: Раздел '{group_name}' не найден\n")
        return

    print(f"\nТОВАРЫ В РАЗДЕЛЕ '{group_name.upper()}':")

    if not shop[group_name]:
        print('  (товары отсутствуют)')
    else:
        for product, price in shop[group_name].items():
            print(f'  - {product}: {price} руб.')

    print()


def change_price(group_name, product_name, percent):
    if group_name not in shop:
        print(f"Ошибка: Раздел '{group_name}' не найден")
        return False

    if product_name not in shop[group_name]:
        print(f"Ошибка: Товар '{product_name}' не найден в разделе '{group_name}'")
        return False

    old_price = shop[group_name][product_name]
    new_price = round(old_price * (1 + percent / 100), 2)
    shop[group_name][product_name] = new_price

    action = 'повышена' if percent > 0 else 'снижена'
    print(f"Цена товара '{product_name}' {action} с {old_price} до {new_price} руб.")

    return True


def remove_group(group_name):
    if group_name in shop:
        del shop[group_name]
        print(f"Раздел '{group_name}' полностью удален")
        return True
    print(f"Ошибка: Раздел '{group_name}' не найден")
    return False


def products_from_user_input(products, products_input):
    try:
        for item in products_input.split(','):
            name, price = item.split(':')
            products[name.strip()] = float(price.strip())
    except ValueError:
        print("Ошибка формата ввода! Используйте формат 'товар:цена, товар:цена'")


def change_price_from_user_unput(group, product):
    try:
        percent = float(input('Введите процент изменения (+ для повышения, - для снижения): ').strip())
        change_price(group, product, percent)
    except ValueError:
        print('Ошибка: введите число для процента изменения')


def add_group(group_name):  # функция для администратора создание раздела
    if group_name not in shop:
        shop[group_name] = {}
        print("Создан новый раздел '{group_name}'")
        return True
    print("Раздел '{group_name}' уже существует")
    return False


def apply_global_price(percent):  # функция для администратора повышение цены всех товаров
    for group in shop.values():
        for product in group:
            group[product] = round(group[product] * (1 + percent / 100), 2)
            print(f" Наценка '{percent}'% применена ко всем товарам")


def add_to_basket(product_name, quantity):  # функция для пользователя добавление в корзину
    product_found = False
    for group in shop.values():
        if product_name in group:
            price = group[product_name]
            if product_name in basket:
                basket[product_name]['quantity'] += quantity
            else:
                basket[product_name] = {'price': price, 'quantity': quantity}
            print(f"Добавлено {quantity} шт. товара '{product_name}' в корзину")
            product_found = True
            break

    if not product_found:
        print(f"Товар '{product_name}' не найден в магазине")

    return product_found


def view_basket():
    if not basket:
        print('Корзина пуста')
        return

    total = 0
    print('ВАША КОРЗИНА')
    for product, data in basket.items():
        cost = data['price'] * data['quantity']
        total += cost
        print(f'{product} - {data["price"]} руб. х {data["quantity"]} = {cost}руб')
        print(f'Общая сумма: {total} руб.')


def checkout():  # функция проверки корзигы
    view_basket()
    if basket:
        total = sum(data['price'] * data['quantity'] for data in basket.values())
        print(f'Покупка совершена. Спасибо за покупку на сумму {total} руб.!')
        basket.clear()
    else:
        print('Корзина пуста!')


def add_feedback():  # функция оставления отзыва
    feedback = input('Введите ваш отзыв или предложение: ').strip()
    if feedback:
        feedbacks.append(feedback)
        print('Спасибо, что оставили отзыв')
    else:
        print('Отзыв не может быть пустым')


def main_menu():  # Главное меню
    while True:
        print('\nГЛАВНОЕ МЕНЮ')
        print('1. Режим администратора')
        print('2. Режим пользователя')
        print('3. Выход')
        choice = input('Выберите режим (1-3): ').strip()

        if choice == '1':
            admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            print("Работа магазина 'Мегамаркет от Артёма' завершена. До свидания!")
            break
        else:
            print('Неверный ввод! Пожалуйста, выберите действие от 1 до 3')


# Меню администратора
def admin_menu():
    while True:
        print('\nРЕЖИМ АДМИНИСТРАТОРА')
        print('1. Добавить товары в раздел')
        print('2. Удалить товар из раздела')
        print('3. Показать все товары')
        print('4. Показать товары раздела')
        print('5. Изменить цену товара')
        print('6. Удалить раздел')
        print('7. Добавить новый раздел')
        print('8. Применить наценку ко всем товарам')
        print('9. Вернуться в главное меню')

        choice = input('Выберите действие (1-9): ').strip()

        if choice == '1':
            products_from_user_input()
        elif choice == '2':
            group = input('Введите название раздела: ').strip()
            product = input('Введите название товара: ').strip()
            remove_product(group, product)
        elif choice == '3':
            print_all_products()
        elif choice == '4':
            group = input('Введите название раздела: ').strip()
            print_group_products(group)
        elif choice == '5':
            group = input('Введите название раздела: ').strip()
            product = input('Введите название товара: ').strip()
            change_price_from_user_unput(group, product)
        elif choice == '6':
            group = input('Введите название раздела для удаления: ').strip()
            remove_group(group)
        elif choice == '7':
            group = input('Введите название нового раздела: ').strip()
            add_group(group)
        elif choice == '8':
            try:
                percent = float(input('Введите процент наценки: ').strip())
                apply_global_price(percent)
            except ValueError:
                print('Ошибка: введите число для процента наценки')
        elif choice == '9':
            break
        else:
            print('Неверный ввод! Пожалуйста, выберите действие от 1 до 9')


def user_menu():  # Меню пользователя
    while True:
        print('\nРЕЖИМ ПОЛЬЗОВАТЕЛЯ')
        print('1. Показать все товары')
        print('2. Показать товары раздела')
        print('3. Добавить товар в корзину')
        print('4. Просмотреть корзину')
        print('5. Оформить покупку')
        print('6. Добавить отзыв или предложение')
        print('7. Вернуться в главное меню')

        choice = input('Выберите действие (1-7): ').strip()

        if choice == '1':
            print_all_products()
        elif choice == '2':
            group = input('Введите название раздела: ').strip()
            print_group_products(group)
        elif choice == '3':
            product = input('Введите название товара: ').strip()
            try:
                quantity = int(input('Введите количество: ').strip())
                add_to_basket(product, quantity)
            except ValueError:
                print('Ошибка: введите целое число для количества')
        elif choice == '4':
            view_basket()
        elif choice == '5':
            checkout()
        elif choice == '6':
            add_feedback()
        elif choice == '7':
            break
        else:
            print('Неверный ввод! Пожалуйста, выберите действие от 1 до 7')


if __name__ == '__main__':
    main_menu()
