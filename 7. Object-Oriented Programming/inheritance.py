# ================================================== #

# Materi 1 : Inheritance #1
class Animal :
    def __init__(self, name, color) :
        self.name = name
        self.color = color

class Cat(Animal) :
    def purr(self) :
        print("Pur...")

class Dog(Animal) :
    def bark(self) :
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

# Soal 1 : Which piece of code shows a new class Spam inheriting from Egg?

# Jawaban 1 : class Spam(Egg) :

# ================================================== #

# Materi 2 : Inheritance #2
class Wolf :
    def __init__(self, name, color) :
        self.name = name
        self.color = color

    def bark(self) :
        print("Grr...")

class Dog3(Wolf) :
    def bark(self) :
        print("Woof")

husky = Dog3("Max", "grey")
husky.bark()

# Soal 2 : What is the result of this code?
class A :
    def method(self) :
        print(1)

class B(A) :
    def method(self) :
        print(2)

B().method()

# Jawaban 2 : 2

# ================================================== #

# Materi 3 : Inheritance #3
class A2 :
    def method(self) :
        print("A2 method")

class B2(A2) :
    def another_method(self) :
        print("B2 method")

class C2(B2) :
    def third_method(self) :
        print("C2 method")

c = C2()
c.method()
c.another_method()
c.third_method()

# Soal 3 : What is the result of this code?
class A3 :
    def a(self) :
        print(1)
    
class B3(A3) :
    def a(self) :
        print(2)

class C3(B3) :
    def c(self) :
        print(3)

c = C3()
c.a()

# Jawaban 3 : 2

# ================================================== #

# Materi 4 : Inheritance #4
class A4 :
    def spam(self) :
        print(1)

class B4(A4) :
    def spam(self) :
        print(2)
        super().spam()

B4().spam()

# Soal 4 : What is the superclass of a class?

# Jawaban 4 : The class it inherits from

# ================================================== #