from item import Potion


class Room:
       def __init__(self, name: str, item=None):
           self.name = name
           self.item = item


if __name__ == "__main__":
    empty = Room("Shop")
    hint = Potion("Hint Potion", 1, "Gives you an extra hint!")
    entrance = Room("Entrance", hint)

    print(empty.name, empty.item)
    print(entrance.name, entrance.item.name)
