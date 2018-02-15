# regular method in class automatically takes instance (self) as first argument
# class method automatically takes class (cls) as first argument, this can be done by adding Decorator
# static method don't pass anything automatically, some logical connection with class
# static method doesn't depend on any instance or class variable

class Employee:

    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # here you can use Employee.raise_amount also
        # class attributes can be accessed by only with class or instance

    @classmethod
    def set_raise_method(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        l = emp_string.split('-')
        pay = int(l[-1])
        first, last = l[:2]
        return cls(first, last, pay)
        # you can write Employee(first, last, pay)
        # cls (class) or Employee is same

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Holiday'
        return 'Work day'


if __name__ == '__main__':
    # emp1 = Employee('Bob', 'Smith', 10000)
    # emp2 = Employee('Sue', 'Jones', 12000)
    # print(emp1.raise_amount)
    # print(Employee.raise_amount)
    # Employee.set_raise_method(1.8)
    # print(emp1.raise_amount)
    # print(Employee.raise_amount)
    # emp_str_1 = 'John-Doe-70000'
    # emp_str_2 = 'Steve-Smith-30000'
    # emp_str_3 = 'Jane-Doe-90000'
    # new_emp1 = Employee.from_string(emp_str_1)
    # print(new_emp1.email)
    # print(new_emp1.pay)
    # new_emp1.apply_raise()
    # print(new_emp1.pay)
    import datetime
    my_date = datetime.date(2018, 2, 12)
    print(Employee.is_workday(my_date))