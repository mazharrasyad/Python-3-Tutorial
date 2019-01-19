# ================================================== #

# Materi 1 : Decorators #1
def decor(func) :
    def wrap() :
        print("============")
        func()
        print("============")
    return wrap

def print_text() :
    print("Hello world!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()

# Soal 1 : What are decorators?

# Jawaban 1 : Functions that modify other functions

# ================================================== #

# Materi 2 : Decorators #2
# def print_text() :
#     print("Hello world!")

# print_text = decor(print_text)

@decor
def print_text2() :
    print("Hello world!")

print_text2()

# Soal 2 : Which statement can be used to achieve the same behavior as my_func = my_dec(my_func)?

# Jawaban 2 : @my_dec

# ================================================== #