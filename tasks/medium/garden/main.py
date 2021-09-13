from gardener import Gardener
from tomato import Tomato
from tomato_bush import TomatoBush

if __name__ == '__main__':
    pomidor1 = Tomato(1)
    pomidor2 = Tomato(2)
    tomato1 = Tomato(3)
    tomato2 = Tomato(4)
    tomatobush1 = TomatoBush(pomidor1, pomidor2)
    tomatobush2 = TomatoBush(tomato1, tomato2)
    gardener = Gardener("Stan Li", tomatobush1, tomatobush2)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    print(len(gardener.harvest()))
