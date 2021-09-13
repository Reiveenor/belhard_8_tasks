"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    name: str
    a_type: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def says(self, name):
        print(f"Кошка {self.name} говорит МЯУ")


class Cat(Animal):

    def says(self, name):
        super().__init__(name)
        return print(f"Кошка {self.name} говорит МЯУ")


class Dog(Animal):

    def says(self, name):
        super().__init__(name)
        return print(f"Собака {self.name} говорит ГАФ")


class Cow(Animal):

    def says(self, name):
        super().__init__(name)
        return print(f"Корова {self.name} говорит МУУУ")


if __name__ == '__main__':
    cat = Cat("Scratch")
    cat.says("Scratch")
    dog = Dog("Ichi")
    dog.says("Ichi")
    cow = Cow("Byrenka")
    cow.says("Byrenka")
