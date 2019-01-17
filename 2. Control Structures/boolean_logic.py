# ================================================== #

# Materi 1 : Boolean Logic
print(1 == 1 and 2 == 2) # True
print(1 == 1 and 2 == 3) # False
print(1 != 1 and 2 == 2) # False
print(2 < 1 and 3 > 6) # False

# Soal 1 : What is the result of this code?
if (1 == 1) and (2 + 2 > 3) :
    print("true")
else :
    print("false")

# Jawaban 1 :
# true

# ================================================== #

# Materi 2 : Boolean Or
print(1 == 1 or 2 == 2) # True
print(1 == 1 or 2 == 3) # True
print(1 != 1 or 2 == 2) # True
print(2 < 1 or 3 > 6) # False

# Soal 2 : Fill in the blanks to print "Welcome".
# age = 15
# money = 500
# if age > 18 __ money > 100 :
#   _____("Welcome")

# Jawaban 2 :
age = 15
money = 500
if age > 18 or money > 100 :
    print("Welcome")

# ================================================== #

# Materi 3 : Boolean Not
print(not 1 == 1) # False
print(not 1 > 7) # True

# Soal 3 : What is the result of this code?
if not True :
    print("1")
elif not (1 + 1 == 3) :
    print("2")
else :
    print("3")

# Jawaban 3 :
# 2

# ================================================== #