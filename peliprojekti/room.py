# room that can hold an item
class Room:
       def __init__(self, name: str, item=None, description: str = ""):
           self.name = name
           self.item = item
           self.description = description
