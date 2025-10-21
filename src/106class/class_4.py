class Quiz:
    """Класс для проведения викторины."""

    def __init__(self, questions):
        self.questions = questions
        self.correct_answers_count = 0
        self.total_questions = len(questions)

    def start_quiz(self):
        """Запуск викторины."""
        print('=== ВИКТОРИНА ===\n')

        for i, question_data in enumerate(self.questions, 1):
            print(f'Вопрос {i}/{self.total_questions}:')
            user_answer = self._ask_question(question_data['question'])
            is_correct = self._check_answer(user_answer, question_data['answer'])
            self._handle_answer_result(is_correct, question_data['answer'])

        self.display_result()

    def _ask_question(self, question):
        """
            question (str): Текст вопроса
        Returns:
            str: Ответ пользователя
        """
        return input(f'{question}\nВаш ответ: ').strip()

    def _check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def _handle_answer_result(self, is_correct, correct_answer):
        """
        is_correct (bool): Правильность ответа
        correct_answer (str): Правильный ответ
        """
        if is_correct:
            print('✅ Верно!\n')
            self.correct_answers_count += 1
        else:
            print(f'❌ Неверно. Правильный ответ: {correct_answer}\n')

    def display_result(self):
        """Выводит итоговый результат викторины."""
        print('=' * 30)
        print('ВИКТОРИНА ЗАВЕРШЕНА!')
        print(f'Правильных ответов: {self.correct_answers_count} из {self.total_questions}')
        print('=' * 30)


# Пример использования
if __name__ == '__main__':
    # Список вопросов для викторины
    quiz_questions = [
        {
            'question': 'Сколько планет в Солнечной системе?',
            'answer': '8',
        },
        {
            'question': 'Какой язык программирования назван в честь комедийного шоу?',
            'answer': 'Python',
        },
        {
            'question': 'Столица Франции?',
            'answer': 'Париж',
        },
    ]

    # Создание и запуск викторины
    quiz = Quiz(quiz_questions)
    quiz.start_quiz()
