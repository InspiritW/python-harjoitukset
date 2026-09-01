# ============================================
# Module 10: Elevator + Building (built in 3 parts)
# ============================================
# See 00_concept_association_between_objects.py, above, first — this module is
# about objects that HOLD other objects (a Building has a list of
# Elevators). That's a new idea on top of plain classes.

# --------------------------------------------
# Part 1 (Exercise 1): Elevator class
# --------------------------------------------
# Steps:
# 1. Define class Elevator, with __init__(self, bottom_floor, top_floor)
#    storing both, plus self.current_floor = bottom_floor (a new
#    elevator always starts at the bottom).
# 2. Add methods floor_up(self) and floor_down(self): each one moves
#    current_floor by 1 (up or down) and prints something like
#    f"Now at floor {self.current_floor}".
# 3. Add go_to_floor(self, target_floor):
#      - while self.current_floor is not yet at target_floor:
#          if target is above current: call self.floor_up()
#          if target is below current: call self.floor_down()
#    (This is a method calling OTHER methods on the same object —
#    that's normal and good.)
# 4. In the main program: create an elevator, e.g. Elevator(0, 10),
#    send it to floor 5 with go_to_floor(5), then send it back to
#    floor 0.


# --------------------------------------------
# Part 2 (Exercise 2): Building class
# --------------------------------------------
# Steps:
# 1. Define class Building, with __init__(self, bottom_floor, top_floor,
#    num_elevators).
# 2. Inside __init__: create `num_elevators` Elevator objects (using a
#    for loop) and store them in a list: self.elevators = [...]
#    Each Elevator needs the same bottom_floor/top_floor as the building.
# 3. Add a method run_elevator(self, elevator_number, target_floor) that
#    finds the right elevator in self.elevators (by its position/index
#    in the list) and calls go_to_floor on it.
# 4. In the main program: create a Building, then call run_elevator a
#    couple times with different elevator numbers and floors.


# --------------------------------------------
# Part 3 (Exercise 3): fire_alarm()
# --------------------------------------------
# Steps:
# 1. Add a method fire_alarm(self) to Building (no parameters).
# 2. Inside: loop through every elevator in self.elevators and send
#    each one to the bottom floor with go_to_floor.
# 3. In the main program: call building.fire_alarm() and watch every
#    elevator head to floor 0.
