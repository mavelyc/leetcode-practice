#object oriented programming in python

class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('Christian', 'Mavely', 500000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)




