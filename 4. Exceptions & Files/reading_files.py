# ================================================== #

# Materi 1 : Reading Files #1
file = open("filename.txt","r")
cont = file.read()
print(cont)
file.close()

# Soal 1 : Rearrange the code to open a file, read its contents, print them, and then close the file.

# Jawaban 1 : 
file = open("test.txt")
cont = file.read()
print(cont)
file.close()

# ================================================== #

# Materi 2 : Reading Files #2
file = open("filename.txt","r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# Soal 2 : How many characters would be in each line printed by this code, if one character is one byte?
file = open("filename.txt","r")
for i in range(21) :
    print(file.read(4))
file.close()

# Jawaban 2 : 4

# ================================================== #

# Materi 3 : Reading Files #3
file = open("filename.txt","r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

# Soal 3 : Fill in the blanks to open a file, read its content and print its length.
# file = ____("filename.txt","r")
# str = file.____()
# print(len(str))
# file.close()

# Jawaban 3 :
file = open("filename.txt","r")
str = file.read()
print(len(str))
file.close()

# ================================================== #

# Materi 4 : Reading Files #4
file = open("filename.txt","r")
print(file.readlines())
file.close()

file = open("filename.txt","r")
for line in file :
    print(line)
file.close()

# Soal 4 : If the file test.txt has 7 lines of content, what will the following expression return? 
len(open("test.txt").readlines())

# Jawaban 4 : 7

# ================================================== #