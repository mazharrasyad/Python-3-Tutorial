# ================================================== #

# Materi 1 : Returning from Functions #1
def max(x,y) :
    if x >= y :
        return x
    else :
        return y

print(max(4,7)) # 7
z = max(8,5)
print(z) # 8

# Soal 1 : Fill in the blanks to define a function that compares the lengths of its arguments and returns the shortest one.
# def shortest_string(x,y) :
#     if len(x) <= ___(y) :
#         ______ x
#     else :
#         ______ y

# Jawaban 1 :
def shortest_string(x,y) :
    if len(x) <= len(y) :
        return x
    else :
        return y

# ================================================== #

# Materi 2 : Returning from Functions #2
def add_numbers(x,y) :
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4,5)) # 9

# Soal 2 : What is the highest number this function prints if called?
def print_numbers() :
    print(1)
    print(2)
    return
    print(4)
    print(6)

# Jawaban 2 : 2

# ================================================== #