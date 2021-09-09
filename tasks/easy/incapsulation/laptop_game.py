"""
Написать класс Laptop (ноутбук), со следующими скрытыми атрибутами:

- cpu_cores - количество ядер процессора
- gpu_total - количество ГБ видеопамяти
- ram_total - количество ГБ ОЗУ

Определить методы:

- инициализатор __init__, с помощью которого присваиваются скрытые атрибуты
- метод can_play(game_name, cpu_cores, gpu_total, ram_total). Если требования игры
  меньше, чем характеристики компьютера, то вывести
  "На данном ПК есть возможность играть в {game_name}"
"""


class Laptop:
    cpu_cores: int
    gpu_total: int
    ram_total: int

    def __init__(self):
        self.cpu_cores = 4
        self.gpu_total = 8
        self.ram_total = 16

    def can_play(self, cpu_cores, gpu_total, ram_total, game_name):
        self.game_name = game_name
        if cpu_cores > self.cpu_cores or gpu_total > self.gpu_total or ram_total > self.ram_total:
            return f"На данном ПК не получится поиграть в {game_name}"
        else:
            return f"На данном ПК есть возможность играть в {game_name}"


if __name__ == '__main__':
    g = Laptop()
    print(g.can_play(3, 7, 12, "Max Payne"))
    print(g.can_play(3, 10, 10, "GTA 12"))
