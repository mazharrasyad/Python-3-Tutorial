# ================================================== #

# Materi 1 : Metacharacters #1
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg") :
    print("Match 1")

if re.match(pattern, "eggspamspamegg") :
    print("Match 2")

if re.match(pattern, "spam") :
    print("Match 3")

# Soal 1 : What would [a^]* match?

# Jawaban 1 : Zero or more repetitions of "a" or "^"

# ================================================== #

# Materi 2 : Metacharacters #2
import re

pattern = r"g+"

if re.match(pattern, "g") :
    print("Match 1")

if re.match(pattern, "gggggggggggggg") :
    print("Match 2")

if re.match(pattern, "abc") :
    print("Match 3")

# Soal 2 : Fill in the blanks to create a pattern that matches strings that contain one or more 42s.
# r"(42)_$"

# Jawaban 2 : r"(42)+$"

# ================================================== #

# Materi 3 : Metacharacters
import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream") :
    print("Match 1")

if re.match(pattern, "icecream") :
    print("Match 2")

if re.match(pattern, "sausages") :
    print("Match 3")

if re.match(pattern, "ice--ice") :
    print("Match 4")

# Soal 3 : Fill in the blanks to match both 'color' and 'colour'.
# pattern = r"colo_u)_r"

# Jawaban 3 : pattern = r"colo(u)?r"

# ================================================== #

# Materi 4 : Curly Braces
import re

pattern = r"9{1,3}$"

if re.match(pattern, "9") :
    print("Match 1")

if re.match(pattern, "999") :
    print("Match 2")

if re.match(pattern, "9999") :
    print("Match 3")

# Soal 4 : Which of these is the same as the metacharacter '+'?

# Jawaban 4 : {1,}

# ================================================== #