# ================================================== #

# Materi 1 : Magic Methods #1
class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def __add__(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# Soal 1 : What is the magic method for creating an instance?

# Jawaban 1 : __init__

# ================================================== #

# Materi 2 : Magic Methods #2
class SpecialString :
    def __init__(self, cont) :
        self.cont = cont

    def __truediv__(self, other) :
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# Soal 2 : What is A() ^ B() evaluated as, if A doesn't implement any magic methods?

# Jawaban 2 : B().__rxor__(A())

# ================================================== #

# Materi 3 : Magic Methods #3
class SpecialString2 :
    def __init__(self, cont) :
        self.cont = cont

    def __gt__(self, other) :
        for index in range(len(other.cont) + 1) :
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString2("spam")
eggs = SpecialString2("eggs")
spam > eggs

# Soal 3 : What is __le__ a magic method for?

# Jawaban 3 : x <= y

# ================================================== #

# Materi 4 : Magic Methods #4
import random

class VagueList :
    def __init__(self, cont) :
        self.cont = cont

    def __getitem__(self, index) :
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self) :
        return random.randint(0, len(self.cont) * 2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

# Soal 4 : Which magic method call is made by x[y] = z?

# Jawaban 4 : x.__setitem__(y, z)

# ================================================== #