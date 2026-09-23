class Item:
    def __init__(self, name):
        self.name = name

class Potion(Item):
    def __init__(self, name: str, cost: float, info: str):
        super().__init__(name)
        self.cost = cost
        self.info = info

if __name__ == "__main__":
    print("item.py was launched directly")
