from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

a = Animal() #Research topic
a.speak()
#Try to create an object of an abstract class Animal that has an abstract method speak(). 
#What error do you get? Also, show how to correctly create a subclass Dog that implements speak() and then create its object.