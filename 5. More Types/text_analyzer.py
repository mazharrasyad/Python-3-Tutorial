# ================================================== #

# Materi 1 : Text Analyzer #1
filename = input("Enter a filename: ")

with open(filename) as f :
    text = f.read()

print(text)

# Soal 1 : Fill in the blanks to read the contents of a file using the "with" statement.
# ____ open(filename) __ f :
#     text = f.read()

# Jawaban 1 :
with open(filename) as f :
    text = f.read()

# ================================================== #

# Materi 2 : Text Analyzer #2
def count_char(text, char) :
    count = 0
    for c in text :
        if c == char :
            count += 1
    return count

filename = input("Enter a filename: ")
with open(filename) as f :
    text = f.read()

print(count_char(text, "r"))

# Soal 2 : Why has the character-counting code been put in a function?

# Jawaban 2 : So it can be run multiple times

# ================================================== #

# Materi 3 : Text Analyzer #3
def count_char2(text, char) :
    count = 0
    for c in text :
        if c == char :
            count += 1
    return count

filename = input("Enter a filename: ")
with open(filename) as f :
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz" :
    perc = 100 * count_char2(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

# Soal 3 : What is the purpose of the round function in the code?

# Jawaban 3 : To reduce the number of digits printed

# ================================================== #