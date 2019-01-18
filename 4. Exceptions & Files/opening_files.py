# ================================================== #

# Materi 1 : Opening Files #1
myfile = open("filename.txt")

# Soal 1 : Which function is used to access files?

# Jawaban 1 : open

# ================================================== #

# Materi 2 : Opening Files #2
# write mode
open("filename.txt","w")

# read mode
open("filename.txt","r")
open("filename.txt")

# binary write mode
open("filename.txt","wb")

# Soal 2 : Drag and drop from the options below to open a file called "test.bin" in binary read mode.
# file = open(_____,_____)

# Jawaban 2 :
file = open("test.bin","rb")

# ================================================== #

# Materi 3 : Opening Files #3
file = open("filename.txt","w")
# do stuff to the file
file.close()

# Soal 3 : How would you close a file stored in a variable "text_file"?

# Jawaban 3 : text_file.close()

# ================================================== #