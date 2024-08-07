class Dog:
    species = "Canis Familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return f"{self.name} says {sound}"

miles=Dog("Miles",4)
miles.description()
miles.speak("woof woof")