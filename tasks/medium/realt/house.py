class House:
    address: str
    area: float
    cost: float

    def __init__(self, address: str, area: float, cost: float):
        self.address = address
        self.cost = cost
        self.area = area

    def increase_cost(self, delta_cost: float):
        self.cost += delta_cost

    def decrease_cost(self, delta_cost: float):
        self.cost -= delta_cost
