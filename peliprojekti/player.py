from room import Room
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
        self.score = 0
        self.solved = set()
    def move(self, destination):
        self.location = destination

if __name__ == "__main__":
    menu = Room("Menu")
    riddle_room = Room("Riddle Room")
    p = Player("Test", menu)
    print(p.name, p.location.name)
    p.move(riddle_room)
    print(p.location.name)