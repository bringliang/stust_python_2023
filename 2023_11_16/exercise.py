class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nAge = {self.age}"

    def myfunc(self):
        print("Hello my name is "+ self.name)

p1=Person('bob',30)
# print(p1)
print(p1.myfunc())