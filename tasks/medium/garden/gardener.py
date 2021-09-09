class Gardener:
    name: str
    plants: list

    def __init__(self, name: str, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        for i in self.plants:
            i.grow_all()

    def harvest(self):
        ready_plants = 0
        for i in self.plants:
            if i.all_are_ripe():
                ready_plants += 1
        if ready_plants == len(self.plants):
            final_tomato_list = []
            for tomato_bush in self.plants:
                final_tomato_list = final_tomato_list + tomato_bush.give_away_all()
            return final_tomato_list
        else:
            print("Ни один томат не созрел")
            return None
