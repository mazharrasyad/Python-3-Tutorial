# ================================================== #

# Soal 1 : Fill in the blanks to define a function that takes two numbers as arguments and returns the smaller one.
# ___ min(x,y) :
#     if x <= y _
#         return x
#     else :
#         ______ y

# Jawaban 1 :
def min(x,y) :
    if x <= y :
        return x
    else :
        return y

# ================================================== #

# Soal 2 : Rearrange the code to define a function that calculates the sum of all numbers from 0 to its argument.

# Jawaban 2 :
def sum(x) :
    res = 0
    for i in range(x) :
        res += i
    return res

# ================================================== #

# Soal 3 : How would you refer to the randint function if it was imported like this? from random import randint as rnd_int

# Jawaban 3 : rnd_int

# ================================================== #

# Soal 4 : What is the highest number output by this code?
def print_nums(x) :
    for i in range(x) :
        print(i)
        return
print_nums(10)

# Jawaban 4 : 0

# ================================================== #

# Soal 5 : What is the output of this code?
def func(x) :
    res = 0
    for i in range(x) :
        res += i
    return res

print(func(4))

# Jawaban 5 : 6

# ================================================== #