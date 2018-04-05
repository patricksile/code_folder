#!/usr/bin/env python3.5
# Python Object_Oriented Programming
# Python Property Decorators - Getters, Setters, and Deleters


class Employee:

    num_of_emps = 0  # Class Variables
    raise_amount = 1.04  # Class Variables

    def __init__(self, first, last):  # Class Initializer
        self.first = first  # Instance variable
        self.last = last    # Instance variable

    @property
    def email(self):  # Methods (functions of the class)
        return '{} {}@gmail.com'.format(self.first, self.last)

    @property   # This is a property decorator.
    def fullname(self):  # Methods (functions of the class)
        return '{} {}'.format(self.first, self.last)

    @fullname.setter    # This is a setter decorator
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter   # This is a deleter decorator
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Omar')

emp_1.first = 'Jim'

emp_1.fullname = 'Patrick Sile'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)
