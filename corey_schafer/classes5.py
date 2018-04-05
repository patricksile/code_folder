#!/usr/bin/env python3.5
# Python Object_Oriented Programming
# Python Special Methods (Magic/Dunder)


class Employee:

    num_of_emps = 0  # Class Variables
    raise_amount = 1.04  # Class Variables

    def __init__(self, first, last, pay):  # Class Initializer
        self.first = first  # Instance variable
        self.last = last    # Instance variable
        self.pay = pay  # Instance variable
        self.email = first + '.' + last + '@gmail.com'  # Instance variable

        Employee.num_of_emps += 1

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

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

emp_1 = Employee('John', 'Omar', 64000)
emp_2 = Employee('Travolta', 'Jack', 100000)

print(emp_1)
print(repr(emp_1))  # Representing the special method __repr__ for the object emp_1
print(str(emp_1))  # Representing the special method __str__ for the object emp_1

# (Same with above) Representing the special method __repr__ for the object emp_1
print(emp_1.__repr__())
# (Same with above) Representing the special method __str__ for the object emp_1
print(emp_1.__str__())

print(1 + 2)
print(int.__add__(1, 2))

print(emp_1 + emp_2)  # Posible because of the dunder method of __add__ configured earlier
print(len(emp_1))
