# ================================================== #

# Materi 1 : Assertions #2
# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# 1
# 2
# Error occurred...
# AssertionError

# Soal 1 : What is the highest number printed by this code?
# print(0)
# assert "h" != "w"
# print(1)
# assert False
# print(2)
# assert True
# print(3)

# Jawaban 1 : 1

# ================================================== #

# Materi 2 : Assertions #2
# temp = -10
# assert (temp >= 0),"Colder than absolute zero!"

# Error occurred...
# AssertionError: Colder than absolute zero!

# Soal 2 : Fill in the blanks to define a function that takes one argument. Assert the argument to be positive.
# ___ my_func(x) :
#     ______ x > 0, "Error"
#     print(x)

# Jawaban 2 :
def my_func(x) :
    assert x > 0, "Error"
    print(x)

# ================================================== #