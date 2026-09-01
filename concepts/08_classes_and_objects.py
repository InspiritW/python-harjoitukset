# ============================================
# Concept: classes and objects (OOP basics)
# ============================================
# A class is a BLUEPRINT for a "thing" that has both data (properties)
# and behavior (methods/functions attached to it).
# An object (or "instance") is one actual thing made from that blueprint.
#
# Real-world analogy: "Dog" the class is the general idea of a dog.
# `my_dog = Dog("Rex")` creates one specific, actual dog named Rex.

# --- Example (run this file as-is) ---
class Dog:
    def __init__(self, name, breed):
        # __init__ runs automatically when you create a new Dog.
        # `self` refers to THIS specific dog object being created.
        self.name = name
        self.breed = breed
        self.energy = 100    # not a parameter — every new dog starts at 100

    def bark(self):
        print(f"{self.name} says Woof!")

    def play(self):
        self.energy -= 10
        print(f"{self.name} played. Energy is now {self.energy}")

# creating objects from the class:
rex = Dog("Rex", "Labrador")
fido = Dog("Fido", "Poodle")

rex.bark()          # "Rex says Woof!"
fido.bark()          # "Fido says Woof!" — same method, different object
rex.play()
print(rex.energy)   # rex and fido have SEPARATE energy values
print(fido.energy)  # this one is still 100

# --- Class variables (a.k.a. static variables) ---
# A normal property (like self.name) belongs to ONE object. A class
# variable belongs to the CLASS ITSELF and is shared by every object
# made from it — useful for things like "how many dogs exist total".
class Cat:
    created = 0   # defined OUTSIDE __init__, no `self.` prefix — this
                   # is what makes it a class variable, not a per-object one

    def __init__(self, name):
        self.name = name          # per-object (each cat has its own name)
        Cat.created = Cat.created + 1   # shared counter, updated via the class

cat1 = Cat("Milo")
cat2 = Cat("Luna")
print(f"{Cat.created} cats created so far")   # 2 — access via the class name

# Naming convention note: class names use CamelCase (Dog, ScreenRectangle),
# no underscores, each word capitalized — you'll see this everywhere.

# --- Your turn ---
# What would you add here to give Dog a `sleep()` method that resets
# energy back to 100? What line inside __init__ would you need to
# change to give each dog a random STARTING energy instead of always 100?
#
# Also: add a class variable to Dog that counts how many Dog objects
# have been created, same pattern as Cat.created above.
