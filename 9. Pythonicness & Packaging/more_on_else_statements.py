# ================================================== #

# Materi 1 : else #1
for i in range(10) :
    if i == 999 :
        break
    else :
        print("Unbroken 1")

for i in range(10) :
    if i == 5 :
        break
    else :
        print("Unbroken 2")

# Soal 1 : What is the largest number this code prints?
for i in range(10) :
    if i > 5 :
        print(i)
        break
    else :
        print("7")

# Jawaban 1 : 6

# ================================================== #

# Materi 2 : else #2
try :
    print(1)
except ZeroDivisionError :
    print(2)
else :
    print(3)

try :
    print(1 / 0)
except ZeroDivisionError :
    print(4)
else :
    print(5)

# Soal 2 : What is the sum of the numbers printed by this code?

# Jawaban 2 :
try :
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError :
    print(3)
else :
    print(4)

# ================================================== #