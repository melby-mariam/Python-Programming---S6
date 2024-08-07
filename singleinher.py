class Vehicle:
    def vehicle_info(self):
        print("Hi Vehicle")

class Car(Vehicle):
    def car_info(self):
        print("Hi Car")

c=Car()
c.vehicle_info()
c.car_info()