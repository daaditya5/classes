# instance.method(arguments) is automatically converted into class.method(instance, arguments)


class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = self.pay * (1 + percent)
        return int(self.pay)

    def __repr__(self):
        return '{} - {}'.format(self.name, self.pay)

    # no difference in using __str__ and __repr__


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, 'Mng', pay)

    def giveRaise(self, percent, bonus = .10):
        return Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    # self test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'Dev', 10000)
    tom = Manager('Tom Hardly', 50000)
    print(bob.name, bob.pay, bob.lastname())
    print(sue.name, sue.pay, sue.lastname(), sue.giveRaise(10))
    print(tom.lastname(), tom.giveRaise(.10, .10))
    print(tom)
    print(sue)
    print(tom.__class__)
    print(Manager.__bases__)
    print(dir(Person))
    print(dir(bob))
    print(bob.__dict__)
    print(bob.__dict__.keys())
    print(bob.__dict__.values())
    l = list(name for name in dir(bob) if not name.startswith('__'))
    print(l)