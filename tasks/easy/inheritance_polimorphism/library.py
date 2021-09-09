"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""


class Person:
    fio: str
    phone: int


class LibraryReader(Person):
    id: int    # noqa A003
    books: list

    def __init__(self, fio, books):
        self.fio = fio
        self.books = books

    def take_books(self, *args):
        for i in args:
            self.books.extend(list(args))
            if len(args) < 4:
                return f"{self.fio} взял книги: {', '.join(args)}"
            else:
                return f"{self.fio} взял {len(args)} книги"

    def return_book(self, *args):
        for i in args:
            if i not in self.books:
                return f"{self.fio} не брал {i}"
            else:
                self.books.remove(i)
                if len(args) < 4:
                    print(f"{self.fio} вернул книги: {', '.join(args)}")
                else:
                    return f"{self.fio} вернул {len(args)} книги"


if __name__ == '__main__':
    lr = LibraryReader("Petrov A.V.", ["Приключения", "Энциклопедия"])
    print(lr.take_books("букварь", "фанфики", "словарь"))
    print(lr.return_book("переводчик"))
