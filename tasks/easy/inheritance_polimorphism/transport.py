"""
Описать класс Transport, у которого следующие атрибуты:

- brand - фирма, выпустившая транспорт
- model - модель
- issue_year - год выпуска
- color - цвет

Определить методы:

- move - который делает raise NotImplementedError

Описать класс Car, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- engine_type

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} проехала {km} километров"

Описать класс Airplane, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- lifting_capacity - грузоподъемность

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} пролетел {km} километров"
"""


class Transport:
    brand: str
    model: int
    issue_year: int
    color: str

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        raise NotImplementedError


class Car(Transport):
    mileage: int
    engine_type: str

    def move(self, km: int, mileage: int):
        super(Car, self).__init__(self.brand, self.model)
        self.mileage = mileage
        self.mileage += km
        return f"{self.brand} {self.model} проехала {km} километров"


class Airplane(Transport):
    mileage: int
    lifting_capacity: int

    def move(self, km: int, mileage: int):
        super(Airplane, self).__init__(self.brand, self.model)
        self.mileage = mileage
        self.mileage += km
        return f"{self.brand} {self.model} пролетел {km} километров"


if __name__ == '__main__':
    c = Car("Toyota", "Camry")
    print(c.move(12, 20))
    print(f"Всего пройденный путь: {c.mileage} км")
    p = Airplane("Boing", 747)
    print(p.move(3000, 1200))
    print(f"Всего пройденный путь: {p.mileage} км")
