# ================================================== #

# Soal 1 : What is the output of this code?
list = [1,1,2,3,5,8,13]
print(list[list[4]])

# Jawaban 1 : 8

# ================================================== #

# Soal 2 : What does this code do?
for i in range(10) :
    if not i % 2 == 0 :
        print(i + 1)

# Jawaban 2 : Print all the even numbers between 2 and 10

# ================================================== #

# Soal 3 : How many lines will this code print?
while False :
    print("Looping...")

# Jawaban 3 : 0

# ================================================== #

# Soal 4 : Fill in the blanks to print the first element of the list, if it contains even number of elements.
# list = [1,2,3,4]
# if ___(list) % 2 == 0 _
#   print(list[_])

# Jawaban 4 :
list = [1,2,3,4]
if len(list) % 2 == 0 :
  print(list[0])

# ================================================== #

# Soal 5 : What does this code output?
letters = ['x','y','z']
letters.insert(1,'w')
print(letters[2])

# Jawaban 5 : y

# ================================================== #

# Soal 6 : Fill in the blanks to iterate over the list using a for loop and print its values.
# list = [1,2,3]
# ___ var __ list :
#     print(___)

# Jawaban 6 :
list = [1,2,3]
for var in list :
    print(var)

# ================================================== #