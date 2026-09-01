# ============================================
# Concept: association — objects that contain other objects
# ============================================
# Once you're comfortable with a single class, the next step is objects
# that HOLD other objects. E.g. a Building doesn't just have a name —
# it has a whole LIST of Elevator objects inside it.
#
# This is normal and powerful: you build small, focused classes, then
# combine them.

# --- Example (run this file as-is) ---
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        # a House "owns" a list of Room objects — this is association
        self.rooms = []
        for i in range(num_rooms):
            room = Room(f"Room {i + 1}")
            self.rooms.append(room)

    def list_rooms(self):
        for room in self.rooms:
            print(room.name)

my_house = House("123 Main St", 3)
my_house.list_rooms()   # Room 1, Room 2, Room 3

# Notice: House's __init__ CREATES the Room objects itself, using a
# loop. This is exactly the pattern module 10 wants for Building
# creating its Elevators.

# --- Permanent vs. temporary association ---
# The House/Room example above is PERMANENT association: House keeps
# self.rooms as a property forever, for as long as the House object exists.
#
# Association can also be TEMPORARY — one object only knows about
# another for the length of a single method call, because it was
# passed in as a parameter, and nothing stores a reference to it:
class Car:
    def __init__(self, plate_number, color):
        self.plate_number = plate_number
        self.color = color

class PaintShop:
    def paint(self, car, new_color):   # `car` only exists inside this call
        car.color = new_color
        # PaintShop never stores `car` anywhere — once paint() returns,
        # this PaintShop object has no memory that this car ever existed.

shop = PaintShop()
my_car = Car("ABC-123", "blue")
shop.paint(my_car, "red")
print(my_car.color)   # "red" — the car WAS changed, but the shop
                        # doesn't remember the car afterwards.
# Compare: if PaintShop had `self.cars_painted = []` and appended `car`
# inside paint(), that would upgrade it to a PERMANENT association.

# --- Your turn ---
# What would you add here to give Room a boolean property `is_occupied`
# (starting False), and a method on House called `find_empty_room()`
# that loops through self.rooms and returns the first one that's
# not occupied?
#
# Also: is the association between PaintShop and Car here unidirectional
# or bidirectional (does the Car know about the PaintShop)? What would
# you need to add to make it bidirectional — and can you think of a
# reason NOT to bother?
