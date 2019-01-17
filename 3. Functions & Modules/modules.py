# ================================================== #

# Materi 1 : Modules #1
import random

for i in range(5) :
    value = random.randint(1,6)
    print(value)

# Soal 1 : Which module is being used in this code?
import math

num = 10
print(math.sqrt(num))

# Jawaban 1 : math

# ================================================== #

# Materi 2 : Modules #2
from math import pi
from math import pi,sqrt

print(pi)

# Soal 2 : Fill in the blanks to import only the sqrt and cos functions from the math module:
# ____ math import _____ cos

# Jawaban 2 :
from math import sqrt, cos

# ================================================== #

# Materi 3 : Modules #3
# import some_module # Error no module named some_module

# Soal 3 : What error is caused by importing an unknown module?

# Jawaban 3 : ImportError

# ================================================== #

# Materi 4 : Modules #4
from math import sqrt as square_root

print(square_root(100))

# Soal 4 : What is the output of this code?
# import math as m

# print(math.sqrt(25)) # Error name math is not defined

# Jawaban 4 : An error occurs

# ================================================== #