"""class Animal():
    def sound(self):
        print("Animal sound: ")


class Dog(Animal):
    def woof(self):
        print("Dog = Woof!\n")


class Cat(Animal):
    def meow(self):
        print("Cat = Meow!\n")


d = Dog()
d.sound()
d.woof()

c=Cat()
c.sound()
c.meow()
"""


class Person():
    def introduce(self, name, age):
        self.name = name
        self.age = age
        return name, age


class Student(Person):
    def introduce(self, name, age, stud_id):
        self.name = name
        self.age = age
        self.stud_id = stud_id
        return name, age, stud_id


s = Student()
intro = s.introduce("John", 20, 1234)
print("Hi, I'm", intro[0], "and I'm", intro[1],
      "years old. My student ID is", intro[2])
