# ================================================== #

# Materi 1 : Classes #1
class Cat :
    def __init__(self, color, legs) :
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# Soal 1 : What type of object is a method?

# Jawaban 1 : Function

# ================================================== #

# Materi 2 : __init__
class Cat2 :
    def __init__(self, color, legs) :
        self.color = color
        self.legs = legs

felix = Cat2("ginger", 4)
print(felix.color)

# Soal 2 : Fill in the blanks to create a class and its constructor, taking one argument and assigning it to the "name" attribute. Then create an object of the class.
# _____ Student :
#     def ________(self, name) :
#         self_____ = name

# test = Student("Bob"_

# Jawaban 2 :
class Student :
    def __init__(self, name) :
        self.name = name

test = Student("Bob")

# ================================================== #

# Materi 3 : Methods
class Dog :
    def __init__(self, name, color) :
        self.name = name
        self.color = color

    def bark(self) :
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

class Dog2 :
    legs = 4
    def __init__(self, name, color) :
        self.name = name
        self.color = color

fido2 = Dog2("Fido", "brown")
print(fido2.legs)
print(Dog2.legs)

# Soal 3 : Fill in the blanks to create a class with a method sayHi().
# class Student _
#     def __init__(self, name) :
#         self.name = name

#     ___ sayHi(____) :
#         print("Hi from " + ____.name)

# s1 = Student("Amy")
# s1.sayHi()

# Jawaban 3 : 
class Student2 :
    def __init__(self, name) :
        self.name = name

    def sayHi(self) :
        print("Hi from " + self.name)

s1 = Student2("Amy")
s1.sayHi()

# ================================================== #

# Materi 4 : Classes #2
class Rectangle :
    def __init__(self, width, height) :
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
# print(rect.color) 
# AttributeError

# Soal 4 : What error is caused by trying to access unknown attributes?

# Jawaban 4 : AttributeError

# ================================================== #