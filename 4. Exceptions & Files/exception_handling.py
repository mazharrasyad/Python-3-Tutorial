# ================================================== #

# Materi 1 : Exception Handling #1
try :
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError :
    print("An error occurred")
    print("due to zero division")

# An error occurred
# due to zero division

# Soal 1 : What is the output of this code?
try :
    variable = 10
    print(10 / 2)
except ZeroDivisionError :
    print("Error")
print("Finished")

# Jawaban 1 : 5.0 Finished

# ================================================== #

# Materi 2 : Exception Handling #2
try :
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError :
    print("Divied by zero")
except (ValueError,TypeError) :
    print("Error occurred")

# Error occurred

# Soal 2 : What is the output of this code?
try :
    meaning = 42
    print(meaning / 0)
    print("the meaning of life")
except (ValueError,TypeError) :
    print("ValueError or TypeError occurred")
except ZeroDivisionError :
    print("Divied by zero")

# Jawaban 2 : Divied by zero

# ================================================== #

# Materi 3 : Exception Handling #3
try :
    word = "spam"
    print(word / 0)
except :
    print("An error occurred")

# An error occurred

# Soal 3 : Fill in the blanks to handle all possible exceptions.
# ____
#     num1 = input(":")
#     num2 = input(":")
#     print(float(num1) / float(num2))
# _______
#     print("Invalid input")

# Jawaban 3 :
try :
    num1 = input(":")
    num2 = input(":")
    print(float(num1) / float(num2))
except :
    print("Invalid input")

# ================================================== #