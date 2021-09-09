from house import House
from person import Person
from townhouse import Townhouse

if __name__ == '__main__':
    house1 = House("address1", 25, 30)
    townhouse1 = Townhouse("address2", 45)
    person = Person("Bomj Valera", 33)
    person.earn_money(15)
    person.make_deal(house1)
    person.info()
    person.earn_money(30)
    person.make_deal(house1)
    person.make_deal(townhouse1)
    person.info()
    # person.earn_money(50)
    # person.make_deal(townhouse1)
    # person.info()
