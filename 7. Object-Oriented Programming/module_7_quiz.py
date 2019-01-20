# ================================================== #

# Soal 1 : How is a property created?

# Jawaban 1 : Using the property decorater

# ================================================== #

# Soal 2 : What is the difference between a class method and a static method?

# Jawaban 2 : Class methods are passed the calling class, static methods aren't

# ================================================== #

# Soal 3 : What are the usual parameter names for the calling instance and the calling class?

# Jawaban 3 : self and cls

# ================================================== #

# Soal 4 : What method is called just before an object is instantiated?

# Jawaban 4 : __init__

# ================================================== #

# Soal 5 : Fill in the blanks to make the egg attribute strongly private and access it from outside of the class.
# class Test :
#     __egg = 7

# t = Test()
# print(t._Test_____)

# Jawaban 5 :
class Test :
    __egg = 7

t = Test()
print(t._Test__egg)

# ================================================== #

# Soal 6 : What is the automatic process by which unnecessary objects are deleted to free memory?

# Jawaban 6 : Garbage collection

# ================================================== #

# Soal 7 : Fill in the blanks to make a setter for the property name.
# class Person :
#     def __init__(self, name) :
#         self._name = name

#     @property
#     def name(self) :
#         return self._name

#     ____________
#     def name(self, value) :
#         self._____ = value

# Jawaban 7 :
class Person :
    def __init__(self, name) :
        self._name = name

    @property
    def name(self) :
        return self._name

    @name.setter
    def name(self, value) :
        self._name = value

# ================================================== #