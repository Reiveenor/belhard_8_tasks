class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Деньги: {self.money}")
        print(f"Список недвижимости: {self.realty}")

    def earn_money(self, cash: float):
        self.money += cash

    def make_deal(self, house):
        if house.cost <= self.money:
            self.money -= house.cost
            self.realty.append(house)
            print(self.realty)
            print(self.money)
        else:
            print("You don't have such money")
