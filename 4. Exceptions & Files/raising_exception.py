# ================================================== #

# Materi 1 : Raising Exceptions #1
# print(1)
# raise ValueError
# print(2)

# 1
# Error Occurred...
# ValueError

# Soal 1 : Which errors occur during the execution of this code?
# try :
#     print(1 / 0)
# except ZeroDivisionError :
#     raise ValueError

# Jawaban 1 : ZeroDivisionError and ValueError

# ================================================== #

# Materi 2 : Raising Exceptions #2
# name = "123"
# raise NameError("Invalid name!")

# Error occurred...
# NameError: Invalid name!

# Soal 2 : Fill in the blanks to raise a ValueError exception, if the input is negative.
# num = input(":")
# if float(num) _ 0 :
#     _____ ValueError("Negative!")

# Jawaban 2 :
num = input(":")
if float(num) < 0 :
    raise ValueError("Negative!")

# ================================================== #

# Materi 3 : Raising Exceptions #3
try :
    num = 5 / 0
except :
    print("An error occurred")
    raise

# An error occurred
# Error occurred...
# ZeroDivisionError: division by error

# Soal 3 : Can you use the raise statement outside the except block?

# Jawaban 3 : Yes

# ================================================== #