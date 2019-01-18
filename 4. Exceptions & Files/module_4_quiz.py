# ================================================== #

# Soal 1 : Which number is not printed by this code?
try : 
    print(1)
    print(20 / 0)
    print(2)
except ZeroDivisionError :
    print(3)
finally :
    print(4)

# Jawaban 1 : 2

# ================================================== #

# Soal 2 : Open the file in binary write mode.
# open("test.txt","w_")

# Jawaban 2 : # open("test.txt","wb")

# ================================================== #

# Soal 3 : Fill in the blanks to try to open and read from a file. Print an error message in case of an exception.
# try :
#     ____ open("test.txt") as _ :
#         print(f.read())
# ______
#     print("Error)

# Jawaban 3 :
try :
    with open("test.txt") as f :
        print(f.read())
except :
    print("Error")    

# ================================================== #

# Soal 4 : What is the highest number that would be printed by this code?
try :
    print(1)
    assert 2 + 2 == 5
except AssertionError :
    print(3)
except :
    print(4)

# Jawaban 4 : 3

# ================================================== #