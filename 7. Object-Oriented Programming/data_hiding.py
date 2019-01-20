# ================================================== #

# Materi 1 : Data Hiding #1
# Encapsulation

# Soal 1 : What is a private method in Python?

# Jawaban 1 : A method external code is discouraged from using

# ================================================== #

# Materi 2 : Data Hiding #2
class Queue :
    def __init__(self, contents) :
        self._hiddenlist = list(contents)

    def push(self, value) :
        self._hiddenlist.insert(0, value)

    def pop(self) :
        return self._hiddenlist.pop(-1)

    def __repr__(self) :
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Soal 2 : What is the purpose of prefacing a method name with a single underscore?

# Jawaban 2 : To mark it as private

# ================================================== #

# Materi 3 : Data Hiding #3
class Spam :
    __egg = 7
    def print_egg(self) :
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg) # AttributeError

# Soal 3 : How would the attribute __a of the class b be accessed from outside the class?

# Jawaban 3 : _b__a

# ================================================== #