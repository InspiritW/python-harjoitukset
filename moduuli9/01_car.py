import random
class Car:
    def __init__(self, regnum: str, maxspeed: int):
        self.regnum = regnum
        self.maxspeed = maxspeed
        self.speed = 0
        self.distance = 0
    def acceleration(self, change: int):
        self.speed += change
        self.speed = max(0,min(self.speed, self.maxspeed))
    def drive(self, hours: int):
        self.distance += self.speed * hours
    


new_car = Car('ABC-123', 142)
print(f"{new_car.regnum, new_car.maxspeed, new_car.distance, new_car.speed}")
new_car.acceleration(30)
new_car.acceleration(70)
new_car.acceleration(50)
print(f"{new_car.speed}")
new_car.acceleration(-200)
print(f"{new_car.speed}")
cars = []
for i in range(0,11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))
for car in cars:
    car.acceleration(car.maxspeed)
hours = 0
while not any (car.distance >= 10000 for car in cars):
    hours += 1
    for car in cars:
        car.acceleration(random.randint(-10, 15))
        car.drive(1)
print(f"Race ended after {hours} hours.")
for car in cars:
    print(f"{car.regnum:<8} {car.speed:>5} {car.distance:>8.1f}")