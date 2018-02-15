class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # def email(self):
    #     return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
        # @property decorator make method into attribute
        # if we add @property decorator to fullname method, we can access as attribute

    def __del__(self):
        return self


if __name__ == '__main__':
    emp1 = Employee('Bob', 'Smith')
    emp2 = Employee('Sue', 'Jones')
    print(emp1.fullname())
    # print(emp1.email())
    print(emp1.email)
    emp1.first = 'John'
    print(emp1.fullname())
    # print(emp1.email())  # here email is a method not a attribute
    print(emp1.email)
    print(emp2.email)
    del emp2
    print(emp2.first)




# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# if __name__ == '__main__':
#     emp1 = Employee('Bob', 'Smith')
#     emp2 = Employee('Sue', 'Jones')
#     print(emp1.fullname())
#     print(emp1.email)
#     emp1.first = 'John'
#     print(emp1.fullname())
#     print(emp1.email)