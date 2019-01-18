# ================================================== #

# Materi 1 : finally #1
try :
    print("Hello")
    print(1 / 0)
except ZeroDivisionError :
    print("Divied by zero")
finally :
    print("This code will run no matter what")

# Hello
# Divided by zero
# This code will run no matter what

# Soal 1 : What is the output of this code?
try :
    print(1)
except :
    print(2)
finally :
    print(3)

# Jawaban 1 : 1 3

# ================================================== #

# Materi 2 : finally #2
# try :
#     print(1)
#     print(10 / 0)
# except ZeroDivisionError :
#     print(unknown_var)
# finally :
#     print("This is executed last")

# 1
# This is executed last
# Error occurred...

# Soal 2 : Drag and drop from the options below to create a try/except/finally block.

# Jawaban 2 :
try :
    print(1)
except :
    print(2)
finally :
    print(42)

# ================================================== #