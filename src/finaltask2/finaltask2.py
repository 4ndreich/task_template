import random
import os


class Game:
    def __init__(self):
        self.words = self.load_words()
        self.current_word = ''
        self.hidden_word = []
        self.guessed_letters = set()
        self.wrong_letters = set()
        self.errors = 0
        self.max_errors = 7
        self.normalization_map = {'ё': 'е', 'й': 'и'}

    def load_words(self):
        """Загрузка слов из файла words.txt"""
        try:
            with open('words.txt', 'r', encoding='utf-8') as file:
                words = [line.strip().lower() for line in file if line.strip()]
            return words if words else self.get_default_words()
        except FileNotFoundError:
            print('Файл words.txt не найден! Используются стандартные слова.')
            return self.get_default_words()

    def get_default_words(self):
        """Возвращает стандартный набор слов"""
        return [
            'программирование',
            'компьютер',
            'алгоритм',
            'библиотека',
            'функция',
            'переменная',
            'разработка',
            'интерфейс',
            'приложение',
            'база данных',
        ]

    def normalize_letter(self, letter):
        """Нормализация букв: ё->е, й->и"""
        letter = letter.lower()
        return self.normalization_map.get(letter, letter)

    def start_new_game(self):
        """Начало новой игры"""
        if not self.words:
            raise ValueError('Нет слов для игры!')

        self.current_word = random.choice(self.words)
        self.hidden_word = ['__' for _ in self.current_word]
        self.guessed_letters = set()
        self.wrong_letters = set()
        self.errors = 0

        # Открываем первую букву
        first_letter = self.normalize_letter(self.current_word[0])
        self.process_letter(first_letter)

        return self.get_game_state()

    def process_letter(self, letter):
        """Обработка введенной буквы"""
        normalized_input = self.normalize_letter(letter)

        # Проверяем, что введена одна буква
        if len(normalized_input) != 1 or not normalized_input.isalpha():
            return False, 'Пожалуйста, введите одну букву!'

        # Проверяем, не вводилась ли уже эта буква
        if normalized_input in self.guessed_letters or normalized_input in self.wrong_letters:
            return False, 'Эта буква уже была!'

        # Проверяем, есть ли буква в слове
        normalized_word_letters = [self.normalize_letter(char) for char in self.current_word]
        if normalized_input in normalized_word_letters:
            self.guessed_letters.add(normalized_input)
            self.update_hidden_word()
            return True, 'Верно!'

        self.wrong_letters.add(normalized_input)
        self.errors += 1
        return True, 'Неверно!'

    def update_hidden_word(self):
        """Обновление отображаемого слова"""
        for index, letter in enumerate(self.current_word):
            normalized_letter = self.normalize_letter(letter)
            if normalized_letter in self.guessed_letters:
                self.hidden_word[index] = letter

    def get_game_state(self):
        """Получение текущего состояния игры"""
        return {
            'hidden_word': ' '.join(self.hidden_word),
            'wrong_letters': ', '.join(sorted(self.wrong_letters)),
            'errors': self.errors,
            'remaining_attempts': self.max_errors - self.errors,
            'is_win': self.check_win(),
            'is_lose': self.check_lose(),
            'current_word': self.current_word,
        }

    def check_win(self):
        """Проверка победы"""
        return '__' not in self.hidden_word

    def check_lose(self):
        """Проверка поражения"""
        return self.errors >= self.max_errors


class ConsoleInterface:
    def __init__(self):
        self.game = Game()
        self.hangman_stages = self.load_hangman_stages()

    def load_hangman_stages(self):
        """Загрузка виселицы из конкретных файлов 0.txt - 7.txt"""
        stages = []
        file_names = [
            '0.txt',
            '1.txt',
            '2.txt',
            '3.txt',
            '4.txt',
            '5.txt',
            '6.txt',
            '7.txt',
        ]

        for file_name in file_names:
            try:
                if os.path.exists(file_name):
                    with open(file_name, 'r', encoding='utf-8') as file:
                        stages.append(file.read())
                else:
                    print(f'Предупреждение: файл {file_name} не найден!')
                    # Создаем простую заглушку
                    stage_num = int(file_name.split('.')[0])
                    stages.append(f'\n=== Стадия {stage_num}/7 ===\n')
            except Exception as error:
                print(f'Ошибка загрузки файла {file_name}: {error}')
                stage_num = int(file_name.split('.')[0])
                stages.append(f'\n=== Стадия {stage_num}/7 ===\n')

        return stages

    def display_game_state(self, game_state):
        """Отображение текущего состояния игры в консоли"""
        # Очищаем консоль
        os.system('cls' if os.name == 'nt' else 'clear')

        # Выводим заголовок
        print('=' * 50)
        print("           ИГРА 'ВИСЕЛИЦА'")
        print('=' * 50)

        # Выводим ASCII-арт виселицы
        stage_index = min(game_state['errors'], 7)
        print(self.hangman_stages[stage_index])

        # Выводим информацию об игре
        print('\n' + '=' * 50)
        print(f'СЛОВО: {game_state["hidden_word"]}')
        wrong_letters_text = game_state['wrong_letters'] if game_state['wrong_letters'] else 'нет'
        print(f'Ошибки ({game_state["errors"]}/7): {wrong_letters_text}')
        print(f'Осталось попыток: {game_state["remaining_attempts"]}')
        print('=' * 50)

        if game_state['is_win']:
            print('\n🎉 ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! 🎉')
        elif game_state['is_lose']:
            print(f'\n💀 ИГРА ОКОНЧЕНА! Загаданное слово: {game_state["current_word"]}')

    def get_user_input(self):
        """Получение ввода от пользователя"""
        while True:
            letter = input("\nВведите букву (или 'выход' для завершения): ").strip()
            if letter.lower() in ['выход', 'exit', 'quit']:
                return None
            if len(letter) == 1 and letter.isalpha():
                return letter
            print("❌ Пожалуйста, введите одну букву или 'выход' для выхода из игры.")

    def play(self):
        """Основной игровой цикл"""
        print("=== ИГРА 'ВИСЕЛИЦА' ===")
        print('Правила: угадайте слово по буквам. Максимум 7 ошибок.')
        print("Буквы 'ё' и 'й' считаются как 'е' и 'и' соответственно.")
        print("Для выхода из игры введите 'выход'")
        input('\nНажмите Enter чтобы начать...')

        game_state = self.game.start_new_game()

        while True:
            self.display_game_state(game_state)

            if game_state['is_win'] or game_state['is_lose']:
                break

            letter = self.get_user_input()
            if letter is None:
                print('Выход из игры...')
                break

            success, message = self.game.process_letter(letter)
            if not success:
                print(f'⚠️  {message}')
                input('Нажмите Enter чтобы продолжить...')
                continue

            print(f'✅ {message}')
            # Небольшая пауза чтобы игрок увидел результат
            if not (game_state['is_win'] or game_state['is_lose']):
                input('Нажмите Enter чтобы продолжить...')

            game_state = self.game.get_game_state()

        # Предложение сыграть еще раз
        if game_state['is_win'] or game_state['is_lose']:
            choice = input('\nХотите сыграть еще раз? (да/нет): ').strip().lower()
            if choice in ['да', 'д', 'yes', 'y', '1']:
                self.game = Game()
                self.play()
            else:
                print('Спасибо за игру! До свидания!')


def check_required_files():
    """Проверка наличия необходимых файлов интерфейса"""
    required_files = [
        '0.txt',
        '1.txt',
        '2.txt',
        '3.txt',
        '4.txt',
        '5.txt',
        '6.txt',
        '7.txt',
    ]
    missing_files = []

    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print('❌ Отсутствуют следующие файлы интерфейса:')
        for file in missing_files:
            print(f'   - {file}')
        print('\nУбедитесь, что все файлы (0.txt - 7.txt) находятся в той же папке, что и программа.')
        return False

    print('✅ Все файлы интерфейса найдены!')
    return True


def create_words_file():
    """Создание файла со словами если он отсутствует"""
    if not os.path.exists('words.txt'):
        print('Создаю файл words.txt...')
        default_words = [
            'программирование',
            'компьютер',
            'алгоритм',
            'библиотека',
            'функция',
            'переменная',
            'разработка',
            'интерфейс',
            'приложение',
            'база данных',
        ]
        with open('words.txt', 'w', encoding='utf-8') as file:
            for word in default_words:
                file.write(word + '\n')
        print('✅ Файл words.txt создан со стандартными словами')


def main():
    """Основная функция"""

    # Проверяем наличие файлов интерфейса
    if not check_required_files():
        print('\nПрограмма не может быть запущена без файлов интерфейса.')
        return

    # Создаем файл со словами если нужно
    create_words_file()

    # Запускаем игру
    try:
        print('\nЗапуск игры...')
        game = ConsoleInterface()
        game.play()
    except KeyboardInterrupt:
        print('\n\nИгра прервана. До свидания!')
    except Exception as error:
        print(f'Произошла непредвиденная ошибка: {error}')


if __name__ == '__main__':
    main()
