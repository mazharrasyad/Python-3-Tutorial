# ================================================== #

# Materi 1 : Sets #1
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

# Soal 1 : What is the output of this code?
letters = {"a", "b", "c", "d"}
if "e" not in letters :
    print(1)
else :
    print(2)

# Jawaban 1 : 1

# ================================================== #

# Materi 2 : Sets #2
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

# Soal 2 : Fill in the blanks to create a set, add the letter "z" to it, and print its length.
# nums = _"a", "b", "c", "d"_
# nums.___("z")
# print(___(nums))

# Jawaban 2 :
nums = {"a", "b", "c", "d"}
nums.add("z")
print(len(nums))

# ================================================== #

# Materi 3 : Sets #3
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

# Soal 3 : What is the output of this code?
a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)

# Jawaban 3 : 3

# ================================================== #

# Materi 4 : Data Structures
# Python supports the following data structures: 
# - Lists
# - Dictionaries
# - Tuples
# - Sets

# Soal 4 : Which of the following data types does not allow duplicate values?

# Jawaban 4 : Sets

# ================================================== #