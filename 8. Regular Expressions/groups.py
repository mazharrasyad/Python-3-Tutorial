# ================================================== #

# Materi 1 : Groups #1
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg") :
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg") :
    print("Match 2")

if re.match(pattern, "spam") :
    print("Match 3")

# Soal 1 : What would '([^aeiou][aeiou][^aeiou])+' match?

# Jawaban 1 : One or more repetitions of a non-vowel, a vowel and a non-vowel

# ================================================== #

# Materi 2 : Groups #2
import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match :
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

# Soal 2 : What would group(3) be of a match of 1(23)(4(56)78)9(0)?

# Jawaban 2 : 56

# ================================================== #

# Materi 3 : Groups #3
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match :
    print(match.group("first"))
    print(match.groups())

# Soal 3 : What would be the result of len(match.groups()) of a match of (a)(b(?:c)(d)(?:e))?

# Jawaban 3 : 3

# ================================================== #

# Materi 4 : Metacharacters
import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match :
    print("Match 1")

match = re.match(pattern, "grey")
if match :
    print("Match 2")

match = re.match(pattern, "griy")
if match :
    print("Match 3")

# Soal 4 : What regex is not equivalent to the others?

# Jawaban 4 : [1-6]

# ================================================== #