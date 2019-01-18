# ================================================== #

# Materi 1 : List Comprehensions #1
# a list comprehension
cubes = [i ** 3 for i in range(5)]
print(cubes)

# Soal 1 : What does this list comprehension create?
nums = [i * 2 for i in range(10)]

# Jawaban 1 : A list of even numbers between 0 and 10

# ================================================== #

# Materi 2 : List Comprehensions #2
evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)

# Soal 2 : Create a list of multiples of 3 from 0 to 20.
# a = _i for i in range(20) __ i % _ == 0]

# Jawaban 2 :
a = [i for i in range(20) if i % 3 == 0]

# ================================================== #

# Materi 3 : List Comprehensions #3
# even = [2 * i for i in range(10 ** 100)]
# MemoryError

# Soal 3 : Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.
# a = [x * 10 ___ x __ range(_, 9)]

# Jawaban 3 :
a = [x * 10 for x in range(5, 9)]

# ================================================== #