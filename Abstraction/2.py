from abc import ABC, abstractmethod
class Vehicle(ABC): 
 @abstractmethod
 def start_engine(self):
    pass
class Car(Vehicle):
 def start_engine(self):
    print("Car engine started")
c = Car()
c.start_engine()
#Create an abstract class Vehicle with an abstract method start_engine().
#Then create a class Car that inherits from Vehicle and implements the start_engine() method to print "Car engine started".