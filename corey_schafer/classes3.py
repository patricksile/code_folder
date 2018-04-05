#!/usr/bin/env python3.5
# Python Object_Oriented Programming
# Differences between regular method (self), class methods (cls) and static methods

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
        "Construct"
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # This is a decorator called classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        "Contruct a method that parses strings to get employee informations"
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # This is a staticmethod decorator
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Patrick', 'Sile', 50000)  # Object with an instance of the Employee class
emp_2 = Employee('Test', 'User', 60000)  # Object with an instance of the Employee class

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


# This will create a new instance(object) of new employee while just parsing a string on the go using the classmetho from_strin(cls, emp_str) whic will return first, last and pay already parse out of the emp_str_1 or 2 or 3 from the database.
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)

import datetime
my_date = datetime.date(2017, 8, 19)

print(Employee.is_workday(my_date))
