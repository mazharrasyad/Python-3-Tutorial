# ================================================== #

# Materi 1 : while Loops #1
i = 1
while i <= 5 :
    print(i)
    i = i + 1

print("Finished!")

# 1
# 2
# 3 
# 4
# 5
# Finished!

# Soal 1 : How many numbers does this code print?
i = 3
while i >= 0 :
    print(i)
    i = i - 1

# 3
# 2
# 1
# 0

# Jawaban 1 :
# 4

# ================================================== #

# Materi 2 : while Loops #2
# while 1 == 1 :
#   print("In the loop")

# In the loop
# In the loop
# In the loop
# ... (Infinite loop)

# Soal 2 : Fill in the blanks to create a loop that increments the value of x by 2 and prints the even values.
# x = 0
# _____ x <= 20 _
#   _____(x)
#   x += 2

# Jawaban 2 :
x = 0
while x <= 20 :
    print(x)
    x += 2

# ================================================== #

# Materi 3 : break
i = 0
while 1 == 1 :
    print(i)
    i = i + 1
    if i >= 5 :
        print("Breaking")
        break

print("Finished")

# 0
# 1
# 2
# 3
# 4
# Breaking
# Finished

# Soal 3 : How many numbers does this code print?
i = 5
while True :
    print(i)
    i = i - 1
    if i <= 2 :
        break

# 5
# 4
# 3

# Jawaban 3 :
# 3

# ================================================== #

# Materi 4 : continue
i = 0
while True :
    i = i + 1
    if i == 2 :
        print("Skipping 2")
        continue
    if i == 5 :
        print("Breaking")
        break
    print(i)

print("Finished")

# 1
# Skipping 2
# 3
# 4
# Breaking
# Finished

# Soal 4 : Which statement ends the current iteration and continues with the next one?

# Jawaban 4 : continue

# ================================================== #