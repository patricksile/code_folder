#!/usr/bin/env python3.5
# Python Object_Oriented Programming
# Classe and instance creation

import sys
print (sys.version)


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Patrick', 'Sile', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)


# print(emp_1.email)
# print(emp_2.email)
#
# print (emp_1.fullname())
# This line is the same as the one bellow: emp_1.fullname()
# This line is the same as the one above: Employee.fullname(emp_1)
print (emp_2.fullname())
