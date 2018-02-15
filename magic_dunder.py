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

    def __repr__(self):
        return '{} - {} - {}'.format(self.fullname(), self.email, self.pay)

    # def __str__(self):
    #     return '{} - {} - {}'.format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


if __name__ == '__main__':
    emp1 = Employee('Bob', 'Smith', 10000)
    emp2 = Employee('Sue', 'Jones', 12000)
    print(emp1)
    print(emp2)
    print(1+2)
    print(int.__add__(1,2))
    print(str.__add__('a', 'b'))
    print(emp1 + emp2)
    print('sukesh'.__len__())
    print(len(emp2))
    print(emp2.fullname())
