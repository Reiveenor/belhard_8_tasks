"""
Создать класс BookCard, в классе должны быть закрытые атрибуты:

- author - автор
- title - название книги
- publishing_house - издательство
- year - год издания
- num_pages - количество страниц
- num_copies - тираж

Определить методы:

- инициализатор __init__
- магические методы сравнения для сортировки книг по году издания

в сеттерах сделать проверки на тип данных. Если тип данных не подходит, то генерировать
ValueError. Для года издания дополнительно проверить на валидность, num_pages и
num_copies должны быть больше 0

реализовать через property
"""
import datetime


class BookCard:
    __author: str
    __title: str
    __house: str
    __year: int
    __num_pages: int
    __num_copies: int

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author
        if not isinstance(author, str):
            raise ValueError

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title
        if not isinstance(title, str):
            raise ValueError

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, house: str):
        self.__house = house
        if not isinstance(house, str):
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year
        format = '%Y'    # noqa A001
        try:
            datetime.datetime.strptime(str(year), format)
            if not isinstance(year, int):
                raise ValueError
        except ValueError:
            print("Incorrect date format, year must have 4 digit")

    @property
    def num_pages(self):
        return self.__num_pages

    @num_pages.setter
    def num_pages(self, num_pages: int):
        self.__num_pages = num_pages
        if not isinstance(num_pages, int) or num_pages <= 0:
            raise ValueError

    @property
    def num_copies(self):
        return self.__num_copies

    @num_copies.setter
    def num_copies(self, num_copies: int):
        self.__num_copies = num_copies
        if not isinstance(num_copies, int) or num_copies <= 0:
            raise ValueError

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __repr__(self):
        return f"<Publication was in {self.__year}, author: {self.__author}>"


if __name__ == '__main__':
    a, b, c, d = BookCard(), BookCard(), BookCard(), BookCard()
    a.author, b.author, c.author, d.author = "Van Goh", "Alan Mur", "Victor von Doom", "Paul Van Daiki"
    a.title, b.title, c.title, d.title = "Some epic title", "Some epic title", "Some epic title", "Some epic title"
    a.house, b.house, c.house, d.house = "publishing_house", "publishing_house", "publishing_house", "publishing_house"
    a.year = 1340
    a.num_pages = 120
    a.num_copies = 500
    b.year = 1285
    b.num_pages = 120
    b.num_copies = 500
    c.year = 1500
    c.num_pages = 120
    c.num_copies = 500
    d.year = 2021
    d.num_pages = 120
    d.num_copies = 500
    books = [a, b, c, d]
print(repr(sorted(books, key=lambda Bookcard: Bookcard.year)))
