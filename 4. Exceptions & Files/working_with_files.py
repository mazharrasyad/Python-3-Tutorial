# ================================================== #

# Materi 1 : Working with Files #1
try :
    f = open("filename.txt")
    print(f.read())
finally :
    f.close()

# Soal 1 : Will the close() function get called in this code?
# try :
#     f = open("filename.txt")
#     print(f.read())
#     print(1 / 0)
# finally :
#     f.close

# Jawaban 1 : Yes

# ================================================== #

# Materi 2 : Working with Files #2
with open("filename.txt") as f :
    print(f.read())

# Soal 2 : Fill in the blanks to create a valid with statement, reading the contents of the file.
# ____ open("test.txt") __ f :
#     print(f.____())

# Jawaban 2 :
with open("test.txt") as f :
    print(f.read())

# ================================================== #