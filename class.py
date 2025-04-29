import time
start_time = time.time()

def is_valid(board, row, col, num):
    # Check if the number is not repeated in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is not repeated in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not repeated in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 10
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

def print_board(board):
    for row in board:
        print(*row)


# Given Sudoku puzzle
sudoku = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

if solve_sudoku(sudoku):
    print("Solution:")
    print_board(sudoku)
else:
    print("No solution")

end_time = time.time()
print("Time:", end_time - start_time)

"""Create a class Person with attributes name and age. Inherit a class Employee that adds salary. Write a method to display all attributes.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printdetails(self):
        print(self.name, self.age)

class Employee(Person):  # subclass
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def printdetails(self):
        print(self.name, self.age, self.salary)

e1 = Employee("John", 30, 50000)
e1.printdetails()

"""Define a class Animal with a method speak(). Inherit it in class Dog and override the speak() method to print "Bark"."""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
      print("Bark")

d1 = Dog()
d1.speak()

"""Make a class Vehicle with a method info() that prints "This is a vehicle". Create a class Car that inherits Vehicle and adds a method brand() which prints the car's brand.

"""

class Vehicle:
    def details(self):
        print("This is a vehicle")

class Car(Vehicle):  # subclass
    def brand(self, brand):
        print("Car brand is:", brand)

c1 = Car()
c1.details()
c1.brand("Toyota")

"""
Build a class Shape with a method area() that returns 0. Inherit a class Square that overrides area() to return area of a square (given side)."""

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(4)
print(s.area())

"""


Write a class Parent with a private variable and a getter method. Inherit a class Child and access the private variable via the getter."""

class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

class Student(Person):
    def display_age(self):
        print(self.get_age())

s = Student(21)
s.display_age()

"""Create two classes Writer and Editor, each with a method role(). Inherit a class Author from both and override role() to describe an author’s combined role."""

class writer:
    def role(self):
        print("Writer")

class editor:
    def role(self):
        print("Editor")

class author(writer, editor):
    def role(self):
        print("Author")

a1 = author()
a1.role()

"""Define a class MathTeacher with a method teach(), and another class BasketballCoach with train(). Make a SchoolStaff class that inherits both and uses both methods.

"""

class MathTeacher:
    def teach(self):
        print(" math")

class BasketballCoach:
    def train(self):
        print("basketball")

class SchoolStaff(MathTeacher, BasketballCoach):
    pass

s1 = SchoolStaff()
s1.teach()
s1.train()

"""Create classes A and B with a method say() that prints different messages. Inherit class C(A, B) and call say(). What gets printed?

"""

class A:
    def say(self):
        print("california burrito")

class B:
    def say(self):
        print("Chocolate fudge")

class C(A, B):
    pass

Food = C()
Food.say()

"""Write a program that demonstrates method resolution order (MRO) using multiple inheritance. Show how Python decides which method to call.


"""



"""Simulate a class Person and class Athlete. Make a subclass StudentAthlete that inherits from both, and demonstrate accessing attributes/methods from both base classes."""

class Person:
    def __init__(self, name):
        print("Hi, I am", name)

class Athlete:
    def __init__(self, sport):
        print("I", sport)

class StudentAthlete(Person, Athlete):
    def __init__(self, name, sport):
        Person.__init__(self, name)
        Athlete.__init__(self, sport)

s1 = StudentAthlete("Esha", "Swim")

"""Create a class Grandparent with a method history(). Inherit Parent from it and add legacy(). Inherit Child from Parent and add future(). Call all three methods from a Child object.


"""

class Grandparent:
    def history(self):
        print("grandparents History")

class Parent(Grandparent):
    def legacy(self):
        print("parents Legacy")

class Child(Parent):
    def future(self):
        print("the Future")
result = Child()
result.history()
result.legacy()
result.future()

"""Make a base class Device with a method specs(). Inherit Phone from Device, and Smartphone from Phone. Override specs() at each level and see which one gets called.


"""

class device:
    def specs(self):
        print("device")

class phone(device):
    def specs(self):
        print("phone")

class smartphone(phone):
    def specs(self):
        print("smartphone")
display = smartphone()
display.specs()

"""Design a multilevel class structure: Organism -> Animal -> Human, each with a method info(). Override the method at each level and call info() from a Human object.


"""

class Organism:
    def info(self):
        print("ORGANISAM")

class Animal(Organism):
    def info(self):
        print("ANIMAL")

class Human(Animal):
    def info(self):
        print("I AM A HUMAN")

result = Human()
result.info()

"""Implement a multilevel inheritance where the base class University has details like name and location, College inherits it with department info, and Student inherits College with personal details. Print complete student info.

"""

class university:
    def __init__(self, name, location):
        self.name = name
        self.location = location
class college(university):
    def __init__(self, name, location, department):
        super().__init__(name, location)
        self.department = department
class student(college):
    def __init__(self, name, location, department,stud_id, age):
        super().__init__(name, location, department)
        self.roll_no = stud_id
        self.age = age
    def info(self):
        print("University:", self.name)
        print("Location:", self.location)
        print("Department:", self.department)
        print("Roll Number:", self.roll_no)
        print("Age:", self.age)

s1 = student("University of North Texas", "Denton", "Business Analytics", 11654812, 24)
s1.info()

"""
Write a multilevel inheritance example with a class A having a method greet(), B(A) adding introduce(), and C(B) adding describe(). Call all three methods from an object of class C."""

class A:
 def greet(self):
     print("Hello from A")

class B(A):
  def introduce(self):
      print("Hello from B")

class C(B):
  def describe(self):
      print("Hello from C")

display = C()
display.greet()
display.introduce()
display.describe()