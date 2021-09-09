"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- x int
- y int

Координаты должны быть доступны для чтения, а их изменение должно происходить в методе
move(delta_x, delta_y)

реализовать через property
"""


class GameObject:
    __x = 10
    __y = 20

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x += delta_x
        self.__y += delta_y
        return delta_x, delta_y


if __name__ == '__main__':
    a = GameObject()
    print(a.move(0, 0))
