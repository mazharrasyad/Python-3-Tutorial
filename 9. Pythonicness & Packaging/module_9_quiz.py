# ================================================== #

# Soal 1 : Which of these isn't a file used in creating a package?

# Jawaban 1 : __py2exe__.py

# ================================================== #

# Soal 2 : What is PEP 8?

# Jawaban 2 : Guidelines for writing code

# ================================================== #

# Soal 3 : What is the output of this code?
def func(**kwargs) :
    print(kwargs["zero"])

func(a = 0, zero = 8)

# Jawaban 3 : 8

# ================================================== #

# Soal 4 : What is sum of the numbers printed by this code?
for i in range(10) :
    try :
        if 10 / i == 2.0 :
            break
    except ZeroDivisionError :
        print(1)
    else :
        print(2)

# Jawaban 4 : 9

# ================================================== #

# Soal 5 : Fill in the blanks to swap the variable values with one single statement.
# a = 7
# b = 42
# a_ b = _, _

# Jawaban 5 :
a = 7
b = 42
a, b = b, a

# ================================================== #