class Vehicle:
    def vehicle_info(self):
        print("Hi Vehicle")

class Car:
    def car_info(self):
        print("Hi Car")

class Sports(Vehicle,Car):
    def sport_info(self):
        print("Hi Sport")
c=Sports()
c.vehicle_info()
c.car_info()
c.sport_info()