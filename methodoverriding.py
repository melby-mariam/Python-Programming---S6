class Employee:
    def WorkingHrs(self):
        self.hrs=50

    def printHrs(self):
        print("Total Working hrs",self.hrs)

class Trainee(Employee):
    def WorkingHrs(self):
        self.hrs=60

    #to reset back to the previous vaalue of working hrs
    def resetHrs(self):
        super().WorkingHrs()

emp=Employee()
emp.WorkingHrs()
emp.printHrs()

tr=Trainee()
tr.WorkingHrs()
tr.printHrs()

#Reset Trainee
tr.resetHrs()
tr.printHrs()