# ================================================== #

# Materi 1 : Recursion #1
def factorial(x) :
    if x == 1 :
        return 1
    else :
        return x * factorial(x-1)

print(factorial(5))

# Soal 1 : What is the base case of a recursive function?

# Jawaban 1 : A case that doesn't involve any further calls to that function

# ================================================== #

# Materi 2 : Recursion #2
def factorial2(x) :
    return x * factorial2(x - 1)

# print(factorial2(5)) 
# RecursionError

# Soal 2 : What is the result of this code?
def sum_to(x) :
    return x + sum_to(x - 1)

# print(sum_to(5))

# Jawaban 2 : RuntimeError

# ================================================== #

# Materi 3 : Recursion #3
def is_even(x) :
    if x == 0 :        
        return True
    else :
        return is_odd(x - 1)

def is_odd(x) :
    return not is_even(x)

# print(is_odd(17))
# print(is_even(23))

# print(is_even(0)) = True
# print(is_even(1)) # print(not is_even(0)) : not True = False
# print(is_even(2)) # print(not is_even(1)) : not False = True
# print(is_even(3)) # print(not is_even(2)) : not True = False

# is_even(0) # True
# print(is_odd(0)) # not is_even(0) : not True # False
# print(is_odd(1)) # not is_even(1) # is_odd(0) # not is_even(0) : not False = True
# print(is_odd(2)) # not is_even(2) # is_odd(1) # not is_even(1) : not True = False
# print(is_odd(3)) # not is_even(3) # is_odd(2) # not is_even(2) : not False = True

# Soal 3 : What is the result of this code?
def fib(x) :
    if x == 0 or x == 1 :
        return 1
    else :
        return fib(x - 1) + fib(x - 2)

print(fib(4))

# Jawaban 3 : 5
# fib(4) : fib(3) + fib(2) : 3 + 2 = 5
# fib(3) : fib(2) + fib(1) : 2 + 1 = 3
# fib(2) : fib(1) + fib(0) : 1 + 1 = 2
# fib(1) : 1
# fib(0) : 1

# ================================================== #