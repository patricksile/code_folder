#!/usr/bin/env python3.5
# Python Object_Oriented Programming
# Python Class Inheritance


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


class Developer(Employee):  # Sub Classing
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # This inherit the init method of the parent class
        # Employee.__init__(self, first, last, pay) # This line does the same as the one above
        self.prog_lang = prog_lang


class Manager(Employee):  # Sub Classing Inheritance

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# dev_1 is an object with an instance of Developer class inheriting for Employee class
dev_1 = Developer('Patrick', 'Sile', 50000, 'Python')
# dev_2 is an object with an instance of Developer class inheriting for Employee class
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Developer))  # To check if an object is an instance of a class
print(issubclass(Developer, Employee))  # To check if a class is a subclass of another class

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# print(mgr_1.email)
# mgr_1.print_emps()

# print(help(Developer))

# print(dev_1.email)
# # dev_1.apply_raise()
# print(dev_1.prog_lang)
