class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Book(Product):
    pass


class Film(Product):
    pass


class Store:
    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print('\nДоступные товары:')
        for i, product in enumerate(self.products, 1):
            product_type = 'Книга' if isinstance(product, Book) else 'Фильм'
            print(f"{i}. {product_type} '{product.name}' - {product.price} руб.")

    def add_to_cart(self, product_index):
        if 0 < product_index <= len(self.products):
            product = self.products[product_index - 1]
            self.cart.append(product)
            print(f"Товар '{product.name}' добавлен в корзину!")
        else:
            print('Неверный номер товара!')

    def calculate_total(self):
        return sum(product.price for product in self.cart)

    def show_cart(self):
        if not self.cart:
            print('\nКорзина пуста!')
            return

        print('\nВаша корзина:')
        for product in self.cart:
            product_type = 'Книга' if isinstance(product, Book) else 'Фильм'
            print(f"- {product_type} '{product.name}': {product.price} руб.")
        print(f'Общая сумма: {self.calculate_total()} руб.')


# Создание товаров
books = [
    Book('Мастер и Маргарита', 450),
    Book('1984', 350),
    Book('Преступление и наказание', 400),
    Book('Война и мир', 600),
    Book('Гарри Поттер и философский камень', 500),
]

films = [
    Film('Крестный отец', 299),
    Film('Побег из Шоушенка', 249),
    Film('Темный рыцарь', 349),
    Film('Начало', 279),
    Film('Форрест Гамп', 199),
]

# Создание  магазина
store = Store()
for book in books:
    store.add_product(book)
for film in films:
    store.add_product(film)

# Работа магазина
if __name__ == '__main__':
    while True:
        print('\n1 - Показать товары')
        print('2 - Добавить товар в корзину')
        print('3 - Показать корзину')
        print('4 - Выйти')

        choice = input('\nВыберите действие: ')

        if choice == '1':
            store.show_products()
        elif choice == '2':
            store.show_products()
            try:
                num = int(input('Введите номер товара: '))
                store.add_to_cart(num)
            except ValueError:
                print('Ошибка ввода!')
        elif choice == '3':
            store.show_cart()
        elif choice == '4':
            break
        else:
            print('Неверный ввод!')
