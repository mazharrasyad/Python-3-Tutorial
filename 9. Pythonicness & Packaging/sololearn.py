# ================================================== #

# Materi 1 : __main__ #1
def function() :
    print("This is a module function")

if __name__ == "__main__" :
    print("This is a script")

# Soal 1 : Which variable couldn't be accessed if this code was imported as a module?
x = 1
y = x
if __name__ == "__main__" :
    z = 3

# Jawaban 1 : z

# ================================================== #

# Materi 2 : __main__ #2
def function2() :
    print("This is a module function")

if __name__ == "__main__" :
    print("This is a script")

# Soal 2 : Rearrange the code to print "Welcome" if the script is imported, and "Hi" if it is not imported.

# Jawaban 2 : 
if __name__ == "__main__" :
    print("Hi")
else :
    print("Welcome")

# ================================================== #