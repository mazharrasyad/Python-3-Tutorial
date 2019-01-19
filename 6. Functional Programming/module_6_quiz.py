# ================================================== #

# Soal 1 : What is the result of this code?
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x : x > 1, nums)
print(len(list(nums)))

# Jawaban 1 : 2

# ================================================== #

# Soal 2 : What is the result of this code?
def power(x, y) :
    if y == 0 :
        return 1
    else :
        return x * power(x, y - 1)

print(power(2, 3))

# power(2, 3)
# 2 * power(2, 2) : 2 * 4 = 8
# 2 * power(2, 1) : 2 * 2 = 4
# 2 * power(2, 0) : 2 * 1 = 2
# power(2, 0) = 1

# Jawaban 2 : 8

# ================================================== #

# Soal 3 : Fill in the blanks to calculate the expression x*(x+1) using an anonymous function and call it for the number 6.
# a = (______ x : x _ (x + 1)) ___
# print(a)

# Jawaban 3 :
a = (lambda x : x * (x + 1)) (6)
print(a)

# ================================================== #

# Soal 4 : Fill in the blanks to leave only even numbers in the list.
# nums = [1, 2, 8, 3, 7]
# res = list(____(______ x : x % _ == 0, nums))
# print(res)

# Jawaban 4 :
nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x : x % 2 == 0, nums))
print(res)

# ================================================== #

# Soal 5 : Drag and drop from the options below to print only the items in the set "a" that are not in the set "b".
# print(_ _ _)

# Jawaban 5 :
# print(a - b)

# ================================================== #