# ============================================
# Module 9: The Car class (built up in 4 parts)
# ============================================
# This whole module is ONE class that grows step by step. Do the parts
# in order, in this same file — don't jump ahead. See
# 00_concept_classes_and_objects.py, above, first if classes are brand new to you.

# --------------------------------------------
# Part 1 (Exercise 1): Basic Car class
# --------------------------------------------
# Steps:
# 1. Define a class called Car.
# 2. Give it an __init__ method (the "initializer") that takes
#    registration_number and max_speed as parameters.
# 3. Inside __init__, store them on the object:
#      self.registration_number = registration_number
#      self.max_speed = max_speed
# 4. Also set two more properties automatically to zero (NOT as
#    parameters — every new car starts with these at 0):
#      self.speed = 0
#      self.distance = 0
# 5. Below the class, in the main program: create one car with
#    registration "ABC-123" and max speed 142.
# 6. Print out all four of its properties.


# --------------------------------------------
# Part 2 (Exercise 2): accelerate() method
# --------------------------------------------
# Steps:
# 1. Inside the Car class, add a method:
#      def accelerate(self, change):
#    `change` can be positive (speed up) or negative (slow down).
# 2. Inside the method: add `change` to self.speed.
# 3. But clamp it! self.speed must never go above self.max_speed, and
#    never below 0. (Look up: how would you cap a value between two
#    limits? Think it through rather than guessing.)
# 4. In the main program: call car.accelerate(30), then
#    car.accelerate(70), then car.accelerate(50). Print the current speed.
# 5. Then call car.accelerate(-200) (emergency brake!) and print the
#    speed again — it should not go below 0.


# --------------------------------------------
# Part 3 (Exercise 3): drive() method
# --------------------------------------------
# Steps:
# 1. Add a method: def drive(self, hours):
# 2. Inside: increase self.distance by (self.speed * hours).
# 3. Try it: if a car has driven 2000 km already and its speed is
#    60 km/h, calling car.drive(1.5) should bring distance to 2090.


# --------------------------------------------
# Part 4 (Exercise 4): The race!
# --------------------------------------------
# Steps:
# 1. Import random.
# 2. Create a list of 10 Car objects using a for loop.
#      - registration numbers: "ABC-1", "ABC-2", ... "ABC-10"
#        (build the string with an f-string using the loop counter)
#      - max_speed: a random value between 100 and 200 for each car
#        (random.randint(100, 200))
# 3. Start a while loop for "one hour of the race passing" that keeps
#    going until some car has driven >= 10000 km.
# 4. Each pass of the loop, for EVERY car in your list (nested for loop):
#      - call car.accelerate(random.randint(-10, 15))
#      - call car.drive(1)
# 5. After the race loop ends, print every car's info in a table.
#    (Tip: an f-string with fixed widths looks like:
#     f"{car.registration_number:<8} {car.speed:>5} {car.distance:>8.1f}")
