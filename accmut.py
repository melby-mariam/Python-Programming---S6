class Car:
    def __init__(self,carname):
        self.__make=carname
    
    def set_make(self,carname):
        self.__make=carname
    def get_make(self):
        return self.__make
mycar=Car('Ford')
print(mycar.get_make())

mycar.set_make('Porche')
print(mycar.get_make())