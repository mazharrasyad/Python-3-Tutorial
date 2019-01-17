# ================================================== #

# Materi 1 : Loops
words = ["hello","world","spam","eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index :
    word = words[counter]
    print(word + "!")
    counter = counter + 1

# hello!
# world!
# spam!
# eggs!

# Soal 1 : Which construct can be used to iterate through a list?

# Jawaban 1 : Loops

# ================================================== #

# Materi 2 : for Loop #1
words = ["hello","world","spam","eggs"]
for word in words :
    print(word + "!")

# hello!
# world!
# spam!
# eggs!

# Soal 2 : Fill in the blanks to create a valid for loop.
# letters = ['a','b','c']
# ___ l __ letters _
#   print(l)

# Jawaban 2 :
letters = ['a','b','c']
for l in letters :
    print(l)

# ================================================== #

# Materi 3 : for Loops #2
for i in range(5) :
    print("hello!")

# hello!
# hello!
# hello!
# hello!
# hello!

# Soal 3 : Fill in the blanks to create a for loop that prints only the even values in the range:
# ___ i in range(0,20,_) :
#   print(_)

# Jawaban 3 :
for i in range(0,20,2) :
    print(i)

# ================================================== #