# ============================================
# Concept: inheritance
# ============================================
# Inheritance lets a class "start from" another class and add or
# change things, instead of writing everything from scratch.
# Say it out loud as "X IS A Y": an ElectricCar IS A Car, with extras.

# --- Example (run this file as-is) ---
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):              # Cat INHERITS from Animal
    def __init__(self, name, indoor):
        super().__init__(name)  # runs Animal's __init__ first (sets self.name)
        self.indoor = indoor    # then adds Cat's own extra property

    def make_sound(self):       # OVERRIDING: Cat has its own version
        print(f"{self.name} says Meow")

generic_animal = Animal("Creature")
generic_animal.make_sound()     # "Creature makes a sound"

my_cat = Cat("Whiskers", True)
my_cat.make_sound()             # "Whiskers says Meow" — uses Cat's version
print(my_cat.name)              # "Whiskers" — inherited from Animal
print(my_cat.indoor)            # True — Cat's own property

# super().__init__(...) is the key trick: it calls the PARENT class's
# initializer so you don't have to repeat `self.name = name` yourself.

# --- Your turn ---
# What would you add here to make a Dog(Animal) class too, with its own
# make_sound() that prints "Woof"? What's the minimum code it needs,
# given that Animal already handles the name?
