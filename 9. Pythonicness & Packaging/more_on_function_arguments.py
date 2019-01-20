# ================================================== #

# Materi 1 : Function Arguments #1
def function(named_arg, *args) :
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# Soal 1 : How is *args accessed inside a function?

# Jawaban 1 : As the tuple args

# ================================================== #

# Materi 2 : Default Values
def function2(x, y, food = "spam") :
    print(food)

function2(1, 2)
function2(3, 4, "egg")

# Soal 2 : What is wrong with this function definition?
# def function(x, y = 7, z, *argums) :

# Jawaban 2 : A non-default argument follows a default argument

# ================================================== #

# Materi 3 : Function Arguments #2
def my_func(x, y = 7, *args, **kwargs) :
    print(kwargs)

my_func(2, 3, 4, 5, 6, a = 7, b = 8)

# Soal 3 : What kind of object is kwargs?

# Jawaban 3 : A dictionary

# ================================================== #