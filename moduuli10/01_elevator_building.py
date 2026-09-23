class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        self.current_floor += 1
        print(f"Now at floor {self.current_floor}")


    def floor_down(self):
        self.current_floor -= 1
        print(f"Now at floor {self.current_floor}")


    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()
            if target_floor < self.current_floor:
                self.floor_down()
e = Elevator(0,10)
e.go_to_floor(5)
e.go_to_floor(e.bottom_floor)


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        self.elevators = []
        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))
    def run_elevator(self, elevator_number, target_floor):
        right_elevator = self.elevators[elevator_number]
        right_elevator.go_to_floor(target_floor)
    def fire_alarm(self): 
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

my_building = Building(0, 10, 3)
my_building.run_elevator(0,5)
my_building.run_elevator(2, 9)
my_building.fire_alarm()



