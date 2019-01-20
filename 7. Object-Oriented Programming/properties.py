# ================================================== #

# Materi 1 : Properties #1
class Pizza :
    def __init__(self, toppings) :
        self.toppings = toppings

    @property
    def pineapple_allowed(self) :
        return False

pizza = Pizza(["cheese", "tomato"])        
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True # AttributeError

# Soal 1 : Fill in the blanks to create an "isAdult" property.
# class Person :
#     def __init__(self, age) :
#         self.age = int(age)

#     _________
#     def isAdult(self) :
#         if self.age > 18 _
#             return True
#         else :
#             ______ False

# Jawaban 1 :
class Person :
    def __init__(self, age) :
        self.age = int(age)

    @property
    def isAdult(self) :
        if self.age > 18 :
            return True
        else :
            return False

# ================================================== #

# Materi 2 : Properties #2
class Pizza2 :
    def __init__(self, toppings) :
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self) :
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value) :
        if value :
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh" :
                self._pineapple_allowed = value
            else :
                raise ValueError("Alert! Intruder!")

pizza = Pizza2(["cheese", "tomato"])                
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

# Soal 2 : Define a decorator that would be used to add a setter to the property egg.

# Jawaban 2 : @egg.setter

# ================================================== #