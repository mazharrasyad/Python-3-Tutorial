# ================================================== #

# Materi 1 : itertools #1
from itertools import count

for i in count(3) :
    print(i)
    if i >= 11 :
        break

# Soal 1 : Fill in the blanks to import the cycle function from the itertools module.
# ____ itertools import _____

# Jawaban 1 : from itertools import cycle

# ================================================== #

# Materi 2 : itertools #2
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x : x <= 6, nums)))

# Soal 2 : Fill in the blanks to take the numbers from the list while they are even, using the takewhile function.
# from itertools ______ takewhile

# nums = [2, 4, 6, 7, 9, 8]
# a = _________(______ x : x % 2 == 0, nums)
# print(list(a))

# Jawaban 2 :
from itertools import takewhile

nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x : x % 2 == 0, nums)
print(list(a))

# ================================================== #

# Materi 3 : itertools #3
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

# Soal 3 : What is the output of this code?
from itertools import product
a = {1, 2}
print(len(list(product(range(3), a))))

# Jawaban 3 : 6

# ================================================== #