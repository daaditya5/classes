class Person:

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

    def info(self):
        return self.name, self.job

    # name, job, age are attributes of instance


p1 = Person('Bob', 'Dev', 27)
p2 = Person('Smith', 'Test', 26)

# Person is class
# p1, p2 are instances (objects) of Person class
# self contain instance (objects) reference or address

print(p1.job)
print(p2.info())

print(type(Person))
print(type(p1))