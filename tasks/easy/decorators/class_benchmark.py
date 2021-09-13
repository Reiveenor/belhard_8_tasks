"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.

До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time


def b_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        start_time = time.time()
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        end_time = time.time()
        print(f"Время окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {end_time - start_time}")
        return result

    return wrapper


class Bench:

    def __init__(self):
        pass

    @b_decorator
    def hello(self, name: str):
        print(f"Привет, {name}")


if __name__ == '__main__':
    b = Bench()
    b.hello(input("Input some name: "))
