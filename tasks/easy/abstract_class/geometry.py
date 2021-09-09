"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    r: int
    pi: float

    def __init__(self, r, pi):
        self.r = r
        self.pi = pi

    def get_perimeter(self):
        super().__init_subclass__()
        r = self.r
        pi = self.pi
        x = 2 * pi * r
        print("Длинна окружности равна: ", x)

    def get_square(self):
        super().__init_subclass__()
        r = self.r
        pi = self.pi
        x = pi * r ** 2
        print("Площадь окружности равна: ", x)


class Rectangle(Shape):
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        super().__init_subclass__()
        a = self.a
        b = self.b
        x = 2 * a + 2 * b
        print("Периметр прямоугольника равен: ", x)

    def get_square(self):
        super().__init_subclass__()
        a = self.a
        b = self.b
        x = a * b
        print("Площадь прямоугольника равна: ", x)


class Square(Rectangle):

    def get_perimeter(self):
        super().__init_subclass__()
        a = self.a
        x = a * 4
        print("Периметр квадрата равен: ", x)

    def get_square(self):
        super().__init_subclass__()
        a = self.a
        x = a ** 2
        print("Площадь квадрата равна: ", x)


if __name__ == '__main__':
    cir = Circle(3, 3.14)
    rec = Rectangle(5, 2)
    sq = Square(5, 5)
    cir.get_perimeter()
    cir.get_square()
    rec.get_perimeter()
    rec.get_square()
    sq.get_perimeter()
    sq.get_square()
