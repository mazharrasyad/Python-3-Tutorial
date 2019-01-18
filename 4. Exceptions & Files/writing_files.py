# ================================================== #

# Materi 1 : Writing Files #1
file = open("newfile.txt","w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt","r")
print(file.read())
file.close()

# Soal 1 : Which line of code writes "Hello world!" to a file?

# Jawaban 1 : file.write("Hello world!")

# ================================================== #

# Materi 2 : Writing Files #2
file = open("newfile.txt","r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt","w")
file.write("Some new text")
file.close()

file = open("newfile.txt","r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

# Soal 2 : What happens if you open a file in write mode and then immediately close it?

# Jawaban 2 : The file contents are deleted

# ================================================== #

# Materi 3 : Writing Files #3
msg = "Hello world!"
file = open("newfile.txt","w")
amount_written = file.write(msg)
print(amount_written)
file.close()

# Soal 3 : If a file write operation is successful, which one of these statements will be true?

# Jawaban 3 : file.write(msg) == len(msg)

# ================================================== #