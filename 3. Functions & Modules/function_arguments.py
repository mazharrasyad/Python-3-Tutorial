# ================================================== #

# Materi 1 : Arguments #1
def print_with_exclamation(word) :
    print(word + "!")

print_with_exclamation("spam") # spam!
print_with_exclamation("eggs") # eggs!
print_with_exclamation("python") # python!

# Soal 1 : What is the result of this code?
def print_double(x) :
    print(2 * x)

print_double(3)

# Jawaban 1 : 6

# ================================================== #

# Materi 2 : Arguments #2
def print_sum_twice(x,y) :
    print(x + y)
    print(x + y)

print_sum_twice(5,8) 

# 13
# 13

# Soal 2 : Fill in the blanks to define a function that takes two arguments and prints their multiplication.
# ___ print_mult(x,y) _
#     print(x * _)

# Jawaban 2 :
def print_mult(x,y) :
    print(x * y)

# ================================================== #

# Materi 3 : Arguments #3
def function(variable) :
    variable += 1
    print(variable)

function(7)
# print(variable) Error name variable is not defined

# Soal 3 : Fill in the blanks to define a function that prints "Yes", if its parameter is an even number, and "No" otherwise.
# ___ even(x) :
#     if x % 2 == 0 :
#         _____("Yes")
#     _____
#         print("No")

# Jawaban 3 :
def even(x) :
    if x % 2 == 0 :
        print("Yes")
    else :
        print("No")

# ================================================== #