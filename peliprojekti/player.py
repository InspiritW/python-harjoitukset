# player data
class Player:
    def __init__(self, name, location, age=0):
        self.name = name
        self.age = age
        self.location = location
        self.items = []
        self.score = 0
        self.solved = set()
        self.recycled = 0
    # changes the room
    def move(self, destination):
        self.location = destination
