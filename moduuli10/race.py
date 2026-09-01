# ============================================
# Module 10, Exercise 4: The Race class
# ============================================
# This continues the Car class race from moduuli9/car.py, part 4 — but
# now wraps the whole race into its own Race class instead of loose code
# in the main program. Copy/import your Car class from module 9 first.
#
# Steps:
# 1. Define class Race with __init__(self, name, distance_km, cars):
#    store all three as properties (self.name, self.distance_km,
#    self.cars — `cars` is a list of Car objects passed in).
# 2. Add method hour_passes(self):
#      - for every car in self.cars: call car.accelerate(random change,
#        e.g. random.randint(-10, 15)), then car.drive(1)
#      (this is the same logic that used to be loose in main — now
#      it lives inside the Race class)
# 3. Add method print_status(self):
#      - print self.name as a header
#      - print every car's info as a formatted table row (reuse the
#        f-string formatting trick from moduuli9/car.py part 4)
# 4. Add method race_finished(self):
#      - return True if ANY car's distance >= self.distance_km,
#        otherwise return False
#
# Main program:
# 1. Create 10 Car objects (like in module 9, part 4).
# 2. Create one Race: Race("Grand Demolition Derby", 8000, your_car_list)
# 3. Loop: call race.hour_passes(). Keep a counter of how many hours
#    have passed. Every 10 hours, call race.print_status().
# 4. Stop the loop when race.race_finished() returns True.
# 5. Call race.print_status() one final time after the loop ends.
