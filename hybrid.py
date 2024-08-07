class Vehicle:
    def vehicle_info(self):
        print("Hi Vehicle")

class Car(Vehicle):
    def car_info(self):
        print("Hi Car")

class Truck(Vehicle):
    def truck_info(self):
        print("Hi Sport")

class sports(Car,Vehicle):
    def sport_info(self):
        print("Hi yessss")

s=sports()
s.vehicle_info()
s.car_info()
s.sport_info()