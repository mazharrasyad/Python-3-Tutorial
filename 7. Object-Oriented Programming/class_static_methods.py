# ================================================== #

# Materi 1 : Class Methods
class Rectangle :
    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def calculate_area(self) :
        return self.width * self.height        

    @classmethod
    def new_square(cls, side_length) :
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

# Soal 1 : Fill in the blanks to make sayHi() a class method.
# class Person :
#     def __init__(self, name) :
#         self.name = name

#     ___________
#     ___ sayHi(cls) :
#         print("Hi")

# Jawaban 1 :
class Person :
    def __init__(self, name) :
        self.name = name

    @classmethod
    def sayHi(cls) :
        print("Hi")

# ================================================== #

# Materi 2 : Static Methods
class Pizza :
    def __init__(self, toppings) :
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping) :
        if topping == "pineapple" :
            raise ValueError("No pineapples!")
        else :
            return True

ingredients = ["cheese", "onions", "spam"]
# ingredients = ["cheese", "onions", "spam", "pineapple"] # ValueError
if all(Pizza.validate_topping(i) for i in ingredients) :
    pizza = Pizza(ingredients)    

# Soal 2 : Which of these is most likely to be a static method?

# Jawaban 2 : def spam(x, y):

# ================================================== #