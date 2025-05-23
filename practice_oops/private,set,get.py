# -*- coding: utf-8 -*-
"""private,set,get.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dmKxMeDBNCn9RnkVmJJfubYBSF0ya71f

Create a class Student with a private attribute __grade. Write a method to set the grade and another to get it.
"""

class student:
   def __init__(self,name,grade):
    self.name=name
    self.__grade=grade
   def set_grade(self, new_grade):
      if new_grade <= 100:
          self.__grade = new_grade
      else:
          self.__grade = "invalid"


   def get_grade(self):
    return self.__grade
a = student("Esha", 90)
print(a.get_grade())
a.set_grade(200)
print(a.get_grade())

"""Create a class BankAccount with attributes __balance (private) and account_holder (public). Add methods to deposit, withdraw, and display balance. Prevent withdrawal if the amount exceeds the balance.

"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, d_amount):
        if d_amount > 0:
            self.__balance += d_amount
            print("Deposited",d_amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, w_amount):
        if w_amount > 0:
            if self.__balance >= w_amount:
                self.__balance -= w_amount
                print("Withdrawn:", w_amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")

    def display_balance(self):
        print("Current balance:",self.__balance)

account = BankAccount("Esha", 1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()

"""Create a class Person with private attributes __name and __age. Use getter and setter methods to access and modify them. Add a condition: age must be between 0 and 120.


"""

class Person:
   def __init__(self,name,age):
     self.__name = name
     self.__age = age
   def get_name(self):
    return self.__name
   def set_age(self,new_age):
     if new_age >=0 and new_age <=120:
        self.__age = new_age
     else:
        self.age = "invalid"
   def get_age(self):
     return self.__age

a = Person("Esha", 24)
print(a.get_name())
a.set_age(25)
print(a.get_age())

"""Write a class Car with a private variable __speed. Create a method to increase the speed but not beyond 200, and another method to display the current speed.


"""

class car:
  def __init__(self,speed):
    self.__speed = speed
  def set_speed(self, new_speed):
    if new_speed <=200:
      self.__speed = new_speed
    else:
      self.__speed ="invalid"
  def get_speed(self):
     return self.__speed

a = car(100)
print("Before speed", a.get_speed())
a.set_speed(200)
print("after set",a.get_speed())

"""Create a class Employee with private attributes __salary and __position. Add methods to update salary only if the position is "Manager". Show how to access these values safely"""

class employee:
  def __init__(self,salary,position):
    self.__salary = salary
    self.__position = position
  def set_salary(self,new_salary):
    if self.__position == "Manager":
      self.__salary = new_salary
    else:
      self.__salary = "invalid"
  def get_salary(self):
    return self.__salary
  def set_position(self,new_position):
    self.__position = new_position
  def get_position(self):
    return self.__position
a = employee(10000,"collegue")
print(a.get_salary())
a.set_salary(20000)
print(a.get_salary())
print(a.get_position())