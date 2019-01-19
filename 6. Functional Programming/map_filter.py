# ================================================== #

# Materi 1 : map
def add_five(x) :
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

result = (list(map(lambda x : x + 5, nums)))
print(result)

# Soal 1 : Fill in the blanks to multiply each item in the list by 2 using lambda syntax.
# nums = [11, 22, 33]
# a = list(map(______ x : ___, ____))

# Jawaban 1 :
nums = [11, 22, 33]
a = list(map(lambda x : x * 2, nums))

# ================================================== #

# Materi 2 : filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x : x % 2 == 0, nums))
print(res)

# Soal 2 : Fill in the blanks to extract all items that are less than 5 from the list.
# nums = [1, 2, 5, 8, 3, 0, 7]
# res = list(______(lambda x : x _ 5, ____))
# print(res)

# Jawaban 2 :
nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x : x < 5, nums))
print(res)

# ================================================== #