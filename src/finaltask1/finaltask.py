import os
import json
import shutil
from typing import Optional


class Book:
    """Представляет отдельную книгу в библиотеке."""

    # Путь к базовой директории библиотеки
    LIBRARY_DIR = 'Library_Books'

    def __init__(self, title: str, book_id: str, chapters_count: int = 0):
        self.title = title
        self.book_id = book_id
        self.chapters_count = chapters_count
        self.folder_path = os.path.join(Book.LIBRARY_DIR, title)
        self.info_file_path = os.path.join(self.folder_path, 'info.json')

    def _save_info(self):
        """Сохраняет информацию о книге в info.json."""
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        data = {
            'id': self.book_id,
            'title': self.title,
            'chapters_count': self.chapters_count,
        }
        with open(self.info_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_chapters(self, count: int):
        """Добавляет главы к книге."""
        self.chapters_count += count
        self._save_info()
        print(f"Книга '{self.title}': добавлено {count} глав. Всего глав: {self.chapters_count}.")

    def remove_chapters(self, count: int):
        """Удаляет главы из книги."""
        if self.chapters_count >= count:
            self.chapters_count -= count
            self._save_info()
            print(f"Книга '{self.title}': удалено {count} глав. Всего глав: {self.chapters_count}.")
        else:
            print(f'Недостаточно глав для удаления. Всего глав: {self.chapters_count}.')

    def delete(self):
        """Удаляет папку книги и все ее содержимое."""
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)
            print(f"Книга '{self.title}' (ID: {self.book_id}) удалена.")
        else:
            print(f"Папка книги '{self.title}' не найдена.")

    def change_title(self, new_title: str):
        """Изменяет название книги и переименовывает папку."""
        new_folder_path = os.path.join(Book.LIBRARY_DIR, new_title)
        if os.path.exists(new_folder_path):
            print(f"Книга с названием '{new_title}' уже существует.")
            return False

        os.rename(self.folder_path, new_folder_path)
        self.title = new_title
        self.folder_path = new_folder_path
        self.info_file_path = os.path.join(self.folder_path, 'info.json')
        self._save_info()
        print(f"Название книги изменено на '{new_title}'.")
        return True

    def display_info(self):
        """Выводит информацию о книге."""
        print(f"  Название: '{self.title}', ID: {self.book_id}, Глав: {self.chapters_count}")


class LibraryManager:
    """Управляет коллекцией книг."""

    def __init__(self):
        self.books = self._load_books()

    def _load_books(self):
        """Загружает существующие книги из файловой системы при запуске."""
        if not os.path.exists(Book.LIBRARY_DIR):
            os.makedirs(Book.LIBRARY_DIR)
            return {}

        books = {}
        for title in os.listdir(Book.LIBRARY_DIR):
            folder_path = os.path.join(Book.LIBRARY_DIR, title)
            info_file_path = os.path.join(folder_path, 'info.json')
            if os.path.isdir(folder_path) and os.path.exists(info_file_path):
                with open(info_file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        book = Book(data['title'], data['id'], data['chapters_count'])
                        books[data['id']] = book
                    except json.JSONDecodeError:
                        print(f'Ошибка чтения файла info.json в папке {title}')
        return books

    def _generate_unique_id(self):
        """Генерирует простой уникальный ID."""
        i = 1
        while str(i) in self.books:
            i += 1
        return str(i)

    def create_book(self):
        """Создает новую книгу через консоль."""
        title = input('Введите название новой книги: ').strip()
        if not title:
            print('Название книги не может быть пустым.')
            return

        for book in self.books.values():
            if book.title == title:
                print(f"Книга с названием '{title}' уже существует.")
                return

        book_id = self._generate_unique_id()
        new_book = Book(title, book_id)
        new_book._save_info()  # Создает папку и файл info.json
        self.books[book_id] = new_book
        print(f"Книга '{title}' успешно создана с ID: {book_id}.")

    def _select_book(self) -> Optional[Book]:
        """Вспомогательная функция для выбора книги по ID."""
        book_id = input('Введите ID книги: ').strip()
        book = self.books.get(book_id)
        if not book:
            print(f"Книга с ID '{book_id}' не найдена.")
        return book

    def add_chapters_to_book(self):
        """Добавляет главы к существующей книге."""
        book = self._select_book()
        if book:
            try:
                count = int(input('Сколько глав добавить? Введите число: ').strip())
                if count > 0:
                    book.add_chapters(count)
                else:
                    print('Введите положительное число.')
            except ValueError:
                print('Некорректный ввод. Введите целое число.')

    # Функция для удаления главы
    def remove_chapters_from_book(self):
        book = self._select_book()
        if book:
            try:
                count = int(input('Сколько глав удалить? Введите число: ').strip())
                if count > 0:
                    book.remove_chapters(count)
                else:
                    print('Введите положительное число.')
            except ValueError:
                print('Некорректный ввод. Введите целое число.')

    def delete_book(self):
        """Удаляет книгу."""
        book = self._select_book()
        if book:
            book.delete()
            del self.books[book.book_id]

    def change_book_title(self):
        """Изменяет название книги."""
        book = self._select_book()
        if book:
            new_title = input('Введите новое название книги: ').strip()
            if new_title:
                if book.change_title(new_title):
                    pass
            else:
                print('Название книги не может быть пустым.')

    def display_all_books(self):
        """Выводит информацию обо всех книгах."""
        if not self.books:
            print('Библиотека пуста.')
        else:
            print('Список книг в библиотеке:')
            for book in self.books.values():
                book.display_info()

    def run_menu(self):
        """Основное меню"""
        while True:
            print('\n--- Меню Электронной Библиотеки ---')
            print('1. Создать книгу')
            print('2. Добавить главы к книге')
            print('3. Удалить главы из книги')
            print('4. Удалить книгу')
            print('5. Изменить название книги')
            print('6. Вывести информацию о всех книгах')
            print('7. Выход')

            choice = input('Выберите действие (1-7): ').strip()

            if choice == '1':
                self.create_book()
            elif choice == '2':
                self.add_chapters_to_book()
            elif choice == '3':
                self.remove_chapters_from_book()
            elif choice == '4':
                self.delete_book()
            elif choice == '5':
                self.change_book_title()
            elif choice == '6':
                self.display_all_books()
            elif choice == '7':
                print('До свидания!')
                break
            else:
                print('Некорректный выбор. Пожалуйста, введите число от 1 до 7.')


if __name__ == '__main__':
    manager = LibraryManager()
    manager.run_menu()
