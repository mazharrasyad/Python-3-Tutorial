# ================================================== #

# Materi 1 : Regular Expressions #1
# Verifying
# Performing

# Soal 1 : Which of the following tasks CANNOT be performed using regular expressions?

# Jawaban 1 : Checking whether an email address is real

# ================================================== #

# Materi 2 : Regular Expressions #2
import re

pattern = r"spam"

if re.match(pattern, "spamspamspam") :
    print("Match")
else :
    print("No match")

# Soal 2 : Which of these patterns would not re.match the string "spamspamspam"?

# Jawaban 2 : pamspam

# ================================================== #

# Materi 3 : Regular Expressions #3
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam") :
    print("Match")
else :
    print("No match")

if re.search(pattern, "eggspamsausagespam") :
    print("Match")
else :
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

# Soal 3 : Which of these is not a function in the re module?

# Jawaban 3 : findlist

# ================================================== #

# Materi 4 : Regular Expressions #4
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match :
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

# Soal 4 : Drag and drop from the options below to print the starting and ending positions of the match.
# import __

# pattern = r"test"
# match = re.search(pattern, "some test")
# print(match._____)
# print(match._____)

# Jawaban 4 :
import re

pattern = r"test"
match = re.search(pattern, "some test")
print(match.start())
print(match.end())

# ================================================== #

# Materi 5 : Search & Replace
import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

# Soal 5 : Fill in the blanks to replace all 9s in the string with 0s.
# import __

# num = "07987549836"
# pattern = r"9"
# num = re.___(pattern, "_", ___)
# print(num)

# Jawaban 5 : 
import re

num = "07987549836"
pattern = r"9"
num = re.sub(pattern, "0", num)
print(num)

# ================================================== #