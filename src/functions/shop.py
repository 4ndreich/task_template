shop = {
    "молочное": {
        "молоко": 100,
    },
    "мучное": {
        "хлеб": 200,
    }
}
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
        else:
            print(f"Ошибка: Товар '{product_name}' не найден в разделе '{group_name}'")
            return False
    else:
        print(f"Ошибка: Раздел '{group_name}' не найден")
        return False
def print_all_products():
    if not shop:
        print("Магазин пуст!")
        return   
    print("\n" + "="*40)
    print("ВСЕ ТОВАРЫ В МАГАЗИНЕ:")
    print("="*40)
    for group, products in shop.items():
        print(f"\nРАЗДЕЛ: {group.upper()}")
        if products:
            for product, price in products.items():
                print(f"  - {product}: {price} руб.")
        else:
            print("  (товары отсутствуют)")
    print("="*40 + "\n")
def print_group_products(group_name):
    if group_name in shop:
        print(f"\nТОВАРЫ В РАЗДЕЛЕ '{group_name.upper()}':")
        if shop[group_name]:
            for product, price in shop[group_name].items():
                print(f"  - {product}: {price} руб.")
        else:
            print("  (товары отсутствуют)")
        print()
    else:
        print(f"Ошибка: Раздел '{group_name}' не найден\n")
def change_price(group_name, product_name, percent):
    if group_name in shop:
        if product_name in shop[group_name]:
            old_price = shop[group_name][product_name]
            new_price = round(old_price * (1 + percent/100), 2)
            shop[group_name][product_name] = new_price
            action = "повышена" if percent > 0 else "снижена"
            print(f"Цена товара '{product_name}' {action} с {old_price} до {new_price} руб.")
            return True
        else:
            print(f"Ошибка: Товар '{product_name}' не найден в разделе '{group_name}'")
            return False
    else:
        print(f"Ошибка: Раздел '{group_name}' не найден")
        return False
def remove_group(group_name):
    if group_name in shop:
        del shop[group_name]
        print(f"Раздел '{group_name}' полностью удален")
        return True
    else:
        print(f"Ошибка: Раздел '{group_name}' не найден")
        return False
def main():
    while True:
        print("МАГАЗИН - ГЛАВНОЕ МЕНЮ")
        print("1. Добавить товары в раздел")
        print("2. Удалить товар из раздела")
        print("3. Показать все товары")
        print("4. Показать товары раздела")
        print("5. Изменить цену товара")
        print("6. Удалить раздел")
        print("7. Выход")
        choice = input("Выберите действие (1-7): ").strip()       
        if choice == '1':
            group = input("Введите название раздела: ").strip()
            products_input = input("Введите товары в формате 'товар:цена, товар:цена': ").strip()
            products = {}
            if products_input:
                try:
                    for item in products_input.split(','):
                        name, price = item.split(':')
                        products[name.strip()] = float(price.strip())
                except ValueError:
                    print("Ошибка формата ввода! Используйте формат 'товар:цена, товар:цена'")
                    continue         
            if products:
                add_products(group, **products)
            else:
                print("Не введены товары для добавления")        
        elif choice == '2':
            group = input("Введите название раздела: ").strip()
            product = input("Введите название товара: ").strip()
            remove_product(group, product)      
        elif choice == '3':
            print_all_products()      
        elif choice == '4':
            group = input("Введите название раздела: ").strip()
            print_group_products(group)        
        elif choice == '5':
            group = input("Введите название раздела: ").strip()
            product = input("Введите название товара: ").strip()
            try:
                percent = float(input("Введите процент изменения (+ для повышения, - для снижения): ").strip())
                change_price(group, product, percent)
            except ValueError:
                print("Ошибка: введите число для процента изменения")        
        elif choice == '6':
            group = input("Введите название раздела для удаления: ").strip()
            remove_group(group)      
        elif choice == '7':
            print("Работа программы завершена. До свидания!")
            break
        else:
            print("Неверный ввод! Пожалуйста, выберите действие от 1 до 7")
if __name__ == "__main__":
    main()
