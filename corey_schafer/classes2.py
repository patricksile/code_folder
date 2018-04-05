#!/usr/bin/env python3.5
# Python Object_Oriented Programming
# Difference between Class Variables and Instance variable
import sys
print (sys.version)


class Employee:

    num_of_emps = 0  # Class Variables
    raise_amount = 1.04  # Class Variables

    def __init__(self, first, last, pay):  # Class Initializer
        self.first = first  # Instance variable
        self.last = last    # Instance variable
        self.pay = pay  # Instance variable
        self.email = first + '.' + last + '@gmail.com'  # Instance variable

        Employee.num_of_emps += 1

    def fullname(self):  # Methods (functions of the class)
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):  # Methods (functions of the class)
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Patrick', 'Sile', 50000)  # Instance (object) of the Employee class
emp_2 = Employee('Test', 'User', 60000)  # Instance (object) of the Employee class
print(Employee.num_of_emps)
print(emp_1.__dict__)   # Checking namespace of the instance
print(emp_2.fullname())
emp_1.raise_amount = 1.07
print(emp_1.__dict__)   # Checking namespace of the instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
