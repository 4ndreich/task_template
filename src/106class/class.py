class Film:
    def __init__(self, movie_title, director, year):
        self.movie_title = movie_title
        self.director = director
        self.year = year

    def display_info(self):
        print(f'Фильм: "{self.movie_title}" | Режиссер: {self.director} | Год: {self.year}')


if __name__ == '__main__':
    films = [
        Film('Побег из Шоушенка', 'Фрэнк Дарабонт', 1994),
        Film('Крестный отец', 'Фрэнсис Форд Коппола', 1972),
        Film('Темный рыцарь', 'Кристофер Нолан', 2008),
    ]

    for film in films:
        film.display_info()
