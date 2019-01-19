# ================================================== #

# Materi 1 : Lambdas #1
def my_func(f, arg) :
    return f(arg)

my_func(lambda x : 2 * x * x, 5)

# Soal 1 : What are anonymous functions called?

# Jawaban 1 : lambdas

# ================================================== #

# Materi 2 : Lambdas #2
# named function
def polynomial(x) :
    return x ** 2 + 5 * x + 4
print(polynomial(-4))

# lambda
print((lambda x : x ** 2 + 5 * x + 4) (-2))

# Soal 2 : Fill in the blanks to create a lambda function that returns the square of its argument, and call it for the number 8.
# a = (______ x _ x * x) (_)

# Jawaban 2 : 
a = (lambda x : x * x) (8)

# ================================================== #

# Materi 3 : Lambdas #3
double = lambda x : x * 2
print(double(7))_____

# Soal 3 : What is the result of this code?
triple = lambda x : x * 3
add = lambda x, y : x + y
print(add(triple(3), 4))

# Jawaban 3 : 13

# ================================================== #