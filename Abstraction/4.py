from abc import ABC, abstractmethod
class shape(ABC):
  @abstractmethod
  def area(self):
    pass
class Square(shape):
  def __init__(self,side):
    self.side=side
  def area(self):
    return self.side**2
class Circle(shape):
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return 3.14*self.radius**2
s=Square(5)
c=Circle(5)
print(s.area())
print(c.area())