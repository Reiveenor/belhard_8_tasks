"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result
    return wrapper


class LoggingMeta(type):
    def __new__(mcs, name, bases, attrs):
        my_class = super().__new__(mcs, name, bases, attrs)
        functions = {key: value for key, value in my_class.__dict__.items() if
                     callable(value) and not key.startswith('_')}
        for key, value in functions.items():
            with_decorator = decorator(value)
            setattr(my_class, key, with_decorator)
        return my_class


class Car(metaclass=LoggingMeta):
    def __init__(self, name: str):
        self.name = name

    def ride(self):
        print(f"Super-duper {self.name} can fly and ride")


delorian = Car("Delorian")
delorian.ride()
print(type(delorian))
