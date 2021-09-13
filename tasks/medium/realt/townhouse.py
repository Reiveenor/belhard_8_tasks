from house import House


class Townhouse(House):
    def __init__(self, address: str, cost: float):
        self.area = 60
        self.address = address
        self.cost = cost
