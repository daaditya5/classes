class Employee:

    num_of_emp = 0
    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # here you can use Employee.raise_amount also
        # class attributes can be accessed by only with class or instance


if __name__ == '__main__':
    print(Employee.num_of_emp)
    emp1 = Employee('Bob', 'Smith', 10000)
    emp2 = Employee('Sue', 'Jones', 12000)
    print(Employee.num_of_emp)
    print(Employee.raise_amount)
    print(emp1.raise_amount)
    print(emp2.raise_amount)
    emp1.apply_raise()
    print(emp1.pay)
    # Employee.raise_amount = 2.5
    # print(Employee.raise_amount)
    # print(emp1.raise_amount)
    # print(emp2.raise_amount)
    emp1.raise_amount = 2.5
    print(Employee.raise_amount)
    print(emp1.raise_amount)
    print(emp2.raise_amount)


