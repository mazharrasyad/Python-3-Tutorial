# ================================================== #

# Materi 1 : Character Classes #1
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey") :
    print("Match 1")

if re.search(pattern, "qwertyuiop") :
    print("Match 2")

if re.search(pattern, "rhythm myths") :
    print("Match 3")

# Soal 1 : What would [abc][def] match?

# Jawaban 1 : Any letter out of "abc", then any out of "def"

# ================================================== #

# Materi 2 : Character Classes #2
import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8") :
    print("Match 1")

if re.search(pattern, "E3") :
    print("Match 2")

if re.search(pattern, "1ab") :
    print("Match 3")

# Soal 2 : What would [1-5][0-9] match?

# Jawaban 2 : Any two-digit number from 10 to 59

# ================================================== #

# Materi 3 : Character Classes #3
import re

pattern = r"[^A-Z]"

if re.search(pattern, "his is all quiet") :
    print("Match 1")

if re.search(pattern, "AbCdEfG123") :
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING") :
    print("Match 3")

# Soal 3 : Fill in the blanks to match strings that are not entirely composed of digits.
# import re

# pattern = r"[_0-9_"

# m = re.search(pattern, "Hi there!")

# Jawaban 3 :
import re

pattern = r"[^0-9]"

m = re.search(pattern, "Hi there!")

# ================================================== #