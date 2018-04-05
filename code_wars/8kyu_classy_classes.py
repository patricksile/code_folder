# Problem: Classy Classes (8kyu)
"""
Classy Classes

Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
Task

Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return
johns age is 34
"""
# My Solution:

class Person:
    def __init__(self, name = "John", age = 34):
        self.name = name
        self.age = age
        self.info = "{}s age is {}".format(self.name,self.age)

# Other Solution:

# Solution 1: By Siebenschlaefer

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return "{0.name}s age is {0.age}".format(self)

p = Person("Patrick", 30)
print(p.info)
