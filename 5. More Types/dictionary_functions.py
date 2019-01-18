# ================================================== #

# Materi 1 : Dictionaries #1
squares = {1:1,2:4,3:"error",4:16,}
squares[8] = 64
squares[3] = 9
print(squares)

# Soal 1 : What is the result of this code?
primes = {1:2, 2:3, 4:7, 7:17}
print(primes[primes[4]])

# Jawaban 1 : 17

# ================================================== #

# Materi 2 : Dictionaries #2
nums = {
    1:"one",
    2:"two",
    3:"three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

# Soal 2 : Drag and drop from the options below to print "Yes", if the key 112 is present in the dictionary named "pairs".
# if ___ ___ ___ :
#     print("Yes")

# Jawaban 2 :
# if 112 in pairs :
#     print("Yes")

# ================================================== #

# Materi 3 : Dictionaries #3
pairs = {
    1:"apple",
    "orange":[2,3,4],
    True:False,
    None:"True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345,"not in dictionary"))

# Soal 3 : What is the result of this code?
fib = {1:1, 2:1, 3:2, 4:3}
print(fib.get(4,0) + fib.get(7,5))

# Jawaban 3 : 8

# ================================================== #