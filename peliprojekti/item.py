# base class for items
class Item:
    def __init__(self, name):
        self.name = name

# item that can be bought
class Potion(Item):
    def __init__(self, name: str, cost: float, info: str):
        super().__init__(name)
        self.cost = cost
        self.info = info

# item that can be recycled
class Scrap(Item):
    def __init__(self, name: str, material: str):
        super().__init__(name)
        self.material = material
