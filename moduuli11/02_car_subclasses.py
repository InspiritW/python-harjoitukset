# ============================================
# Module 11, Exercise 2: ElectricCar / GasolineCar
# ============================================
# Goal: extend your Car class from module 9 with two subclasses that add
# one extra property each.
#
# Steps:
# 1. Copy your Car class from moduuli9/01_car.py (parts 1-3 are enough —
#    you need __init__, accelerate, and drive) into this file, or
#    import it if you're comfortable with that.
# 2. Define class ElectricCar(Car). Its __init__(self, registration_number,
#    max_speed, battery_kwh) should:
#      - call super().__init__(registration_number, max_speed)
#      - then set self.battery_kwh = battery_kwh
# 3. Define class GasolineCar(Car) the same way, but with
#    tank_liters instead of battery_kwh.
# 4. In the main program:
#      - create ElectricCar("ABC-15", 180, 52.5)
#      - create GasolineCar("ACD-123", 165, 32.3)
# 5. Pick a speed for each (accelerate), then call drive(3) on both
#    (drive for 3 hours).
# 6. Print out the distance ("kilometer counter") for both cars.
