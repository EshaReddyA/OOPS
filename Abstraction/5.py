#Create an abstract class Employee with:A constructor that takes name An abstract method get_role()Then create a subclass Manager that prints the employee’s name and returns "Manager" as the role.
from abc import ABC, abstractmethod
class Employee:
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def get_role(self):
        pass
class Manager(Employee):
    def get_role(self):
        return "Manager"
m=Manager("John")
print(m.name)
print(m.get_role())
