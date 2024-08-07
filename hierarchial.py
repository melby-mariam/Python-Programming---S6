class Vehicle:
    def vehicle_info(self):
        print("Hi Vehicle")

class Car(Vehicle):
    def car_info(self):
        print("Hi Car")

class Truck(Vehicle):
    def truck_info(self):
        print("Hi Sport")

s=Truck()
s.vehicle_info()
s.truck_info()

c=Car()
c.vehicle_info()
c.car_info()

