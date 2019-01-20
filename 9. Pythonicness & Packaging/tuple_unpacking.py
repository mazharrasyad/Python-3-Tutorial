# ================================================== #

# Materi 1 : Tuple Unpacking #1
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# Soal 1 : What is the value of y after this code runs?
x, y = [1, 2]
x, y = y, x

# Jawaban 1 : 1

# ================================================== #

# Materi 2 : Tuple Unpacking #2
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# Soal 2 : What is the output of this code?
a, b, c, d, *e, f, g = range(20)
print(len(e))

# Jawaban 2 : 14

# ================================================== #