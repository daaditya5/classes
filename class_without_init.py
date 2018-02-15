class C:

    def setname(self, name):
        self.name = name
        # self default, you can use any word


i1 = C()
i2 = C()

# print(i1.name)
# print(i2.name) # you need to call setname method to access .name attribute

i1.setname('Bob')
i2.setname('Smith')

print(i1.name)
print(i2.name)

# -----------------------------------------------------------------------------------------

# simplest python class

class Rec: pass

Rec.name = 'Dudka'
Rec.age = 27

print(Rec.name)

# -----------------------------------------------------------------------------------------

# or

class rec: pass

r1 = rec()
r2 = rec()

r1.name = 'Sukesh'
r1.age = 27

r2.name = 'Kumar'
r2.age = 27

print(r1.name)
print(r2.name)

r1.name = 'Aadithya'

print(r1.name, r2.name, Rec.name)

# -----------------------------------------------------------------------------------------


class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


# setdata and display are the attributes of class FirstClass
# FirstClass.setdata and FirstClass.display

# Function inside a class called method and they are coded in def

x = FirstClass()
y = FirstClass()

x.setdata('sukesh')
y.data = 'kumar'

x.display()
y.display()

# you can change the value of an attribute
x.data = 'Aarya'
x.display()
x.another = 'Aadithya'
print(x.another)