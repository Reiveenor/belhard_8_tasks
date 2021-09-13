"""
Создать класс Warrior

Определить атрибуты:

- name - имя юнита
- health_points - int от 0 до 100

Определить методы:

- инициализатор __init__, который создает юнита со 100 health_points
- метод hit, который реализует удар, от которого снимается 20 health_points
  у другого юнита

Создать список, в который добавить 5 объектов класса Warrior.

В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение, какой юнит атаковал,
и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья он удаляется из списка.
Программа завершается, когда останется один юнит, на экран выводится сообщение о том,
кто одержал победу.
"""
import random


class Warrior:
    name: str
    health_points: int

    def __init__(self, name: str, health_points: int = 100):
        self.name = name
        self.health_points = health_points

    def hit(self, enemy):
        enemy.health_points -= 20
        print(f"{self.name} в атаке,у противника осталось {enemy.health_points} хитов")


if __name__ == '__main__':
    war_list = [
        Warrior("Sub-zero"),
        Warrior("Scorpion"),
        Warrior("Kung Lao"),
        Warrior("Raiden"),
        Warrior("Sonya")
    ]

    while len(war_list) > 1:
        war1_i, war2_i = random.sample(range(0, len(war_list)), 2)
        war1, war2 = war_list[war1_i], war_list[war2_i]
        war1.hit(war2)
        if war2.health_points == 20:
            print("!!!FINISH HIM!!!")
        if war2.health_points == 0:
            print(f"{war_list[war2_i].name} is dead, !!!FATALITY!!!")
            del war_list[war2_i]
    print(f"{war_list[0].name} is our champion!!!")
