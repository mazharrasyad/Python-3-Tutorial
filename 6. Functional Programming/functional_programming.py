# ================================================== #

# Materi 1 : Functional Programming
def apply_twice(func, arg) :
    return func(func(arg))

def add_five(x) :
    return x + 5

print(apply_twice(add_five, 10)) # 20

# Soal 1 : What is the output of this code?
def test(func, arg) :
    return func(func(arg))

def mult(x) :
    return x * x

print(test(mult, 2))

# Jawaban 1 : 16

# ================================================== #

# Materi 2 : Pure Functions #1
def pure_function(x, y) :
    temp = x + 2 * y
    return temp / (2 * x + y)

some_list = []

def impure(arg) :
    some_list.append(arg)

# Soal 2 : Is this a pure function?
def func(x) :
    y = x ** 2
    z = x + y
    return z

# Jawaban 2 : Yes

# ================================================== #

# Materi 3 : Pure Functions #2
# - easier to reason about, test, and run in parallel
# - more efficient

# Soal 3 : Which of these is not an advantage of using pure functions?

# Jawaban 3 : They are easier to write

# ================================================== #