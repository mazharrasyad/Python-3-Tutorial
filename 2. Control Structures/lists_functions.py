# ================================================== #

# Materi 1 : List Functions #1
nums = [1,2,3]
nums.append(4)
print(nums) # [1,2,3,4]

# Soal 1 : What is the result of this code?
words = ["hello"]
words.append("world")
print(words[1])

# Jawaban 1 : world

# ================================================== #

# Materi 2 : List Functions #2
nums = [1,3,5,2,4]
print(len(nums)) # 5

# Soal 2 : What is the result of this code?
letters = ["a","b","c"]
letters.append("d")
print(len(letters))

# Jawaban 2 : 4

# ================================================== #

# Materi 3 : List Functions #3
words = ["Python","fun"]
index = 1
words.insert(index,"is")
print(words) # ['Pyhton','is','fun']

# Soal 3 : What is the result of this code?
nums = [9,8,7,6,5]
nums.append(4)
nums.insert(2,11)
print(len(nums))

# Jawaban 3 : 7

# ================================================== #

# Materi 4 : List Functions #4
letters = ['p','q','r','s','p','u']
print(letters.index('r')) # 2
print(letters.index('p')) # 0
# print(letters.index('z')) Error z is not in list

# Soal 4 : Drag and drop from the options below to add 'z' to the end of the list and print the list's length.
# list._____('z')
# print(_____ _____)
# (list) index append insert len

# Jawaban 4 :
# list.append('z')
# print(len(list))

# ================================================== #