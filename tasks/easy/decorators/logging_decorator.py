"""
Написать логгирующий декоратор, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result

    return wrapper


class Bench:

    def __init__(self):
        pass

    @log_decorator
    def hello(self, name: str):
        print(f"Привет, {name}")


if __name__ == '__main__':
    b = Bench()
    b.hello(input("Input some name: "))
