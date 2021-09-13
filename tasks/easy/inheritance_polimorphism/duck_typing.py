"""
Создать 3 класса:

Cat, Duck, Cow

в каждом классе определить метод says()

Cat.says() - кошка говорит мяу
Duck.says() - утка говорит кря
Cow.says() - корова говорит муу


Написать функцию animal_says(), которая принимает объект и вызывает метод says
"""


class Cat:
    def say(self):
        return "Кошка говорит мяу"


class Duck:
    def say(self):
        return "Утка говорит кря"


class Cow:
    def say(self):
        return "Корова говорит муу"


def animal_says(animal):
    return animal.say()


if __name__ == '__main__':
    cat = Cat()
    duck = Duck()
    cow = Cow()
    print(animal_says(cat))
    print(animal_says(duck))
    print(animal_says(cow))
