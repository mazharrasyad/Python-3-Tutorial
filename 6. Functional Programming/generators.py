# ================================================== #

# Materi 1 : Generators #1
def countdown() :
    i = 5
    while i > 0 :
        yield i
        i -= 1

for i in countdown() :
    print(i)

# Soal 1 : What statement is used in functions to turn them into generators?

# Jawaban 1 : yield

# ================================================== #

# Materi 2 : Generators #2
def infinite_sevens() :
    while True :
        yield 7

# for i in infinite_sevens() :
#     print(i)

# Soal 2 : Fill in the blanks to create a prime number generator, that yields all prime numbers in a loop. (Consider having an is_prime function already defined):
# ___ get_primes() :
#     num = 2
#     while True :
#         if is_prime(num) :
#             _____ num
#         num += 1

# Jawaban 2 :
# def get_primes() :
#     num = 2
#     while True :
#         if is_prime(num) :
#             yield num
#         num += 1

# ================================================== #

# Materi 3 : Generators #3
def numbers(x) :
    for i in range(x) :
        if i % 2 == 0 :
            yield i

print(list(numbers(11)))

# Soal 3 : What is the result of this code?
def make_word() :
    word = ""
    for ch in "spam" :
        word += ch
        yield word

print(list(make_word()))

# Jawaban 3 : ['s', 'sp', 'spa', 'spam']

# ================================================== #