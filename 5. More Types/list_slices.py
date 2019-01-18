# ================================================== #

# Materi 1 : List Slices #1
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) # [4, 9, 16, 25]
print(squares[3:8]) # [9, 16, 25, 36, 49]
print(squares[0:1]) # [0]

# Soal 1 : What is the result of this code?
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

# Jawaban 1 : [16, 25, 36]

# ================================================== #

# Materi 2 : List Slices #2
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# Soal 2 : Fill in the blanks to take the first two elements of the list:
# list = ["a", "b", "c", "d"]
# a = list[0__]

# Jawaban 2 :
list = ["a", "b", "c", "d"]
a = list[0:2]

# ================================================== #

# Materi 3 : List Slices #3
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

# Soal 3 : What is the output of this code?
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

# Jawaban 3 : [1, 25, 81]

# ================================================== #

# Materi 4 : List Slices #4
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# Soal 4 : What is the output of this code?
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

# Jawaban 4 : [49, 36]

# ================================================== #