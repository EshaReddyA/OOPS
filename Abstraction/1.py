from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine turned on")

    def turn_off(self):
        print("Washing machine turned off")

wm = WashingMachine()
wm.turn_on()
wm.turn_off()
#Define an abstract class Appliance with two abstract methods: turn_on() and turn_off(). 
#Create a class WashingMachine that inherits from Appliance and implements both methods with appropriate print statements.
