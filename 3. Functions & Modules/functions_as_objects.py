# ================================================== #

# Materi 1 : Functions #1
def multiply(x,y) :
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a,b)) # 28

# Soal 1 : What is the output of this code?
def shout(word) :
    return word + "!"
speak = shout
output = speak("shout")
print(output)

# Jawaban 1 : shout!

# ================================================== #

# Materi 2 : Functions #2
def add(x,y) :
    return x + y

def do_twice(func,x,y) :
    return func(func(x,y),func(x,y))

a = 5
b = 10
print(do_twice(add,a,b)) # 30

# Soal 2 : Fill in the blanks to pass the function "square" as an argument to the function "test":
# ___ square(x) :
#     return x * x

# def test(func,x) _
#     print(func(x))

# test(______,42)

# Jawaban 2 :
def square(x) :
    return x * x

def test(func,x) :
    print(func(x))

test(square,42)

# ================================================== #