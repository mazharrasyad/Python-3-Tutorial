# ================================================== #

# Materi 1 : Special Sequences #1
import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match :
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match :
    print("Match 2")

match = re.match(pattern, "abc cde")
if match :
    print("Match 3")

# Soal 1 : What would (abc|xyz)\1 match?

# Jawaban 1 : "abc" or "xyz", followed by the same thing

# ================================================== #

# Materi 2 : Special Sequences #2
import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match :
    print("Match 1")

match = re.match(pattern, "1, 23, 456")
if match :
    print("Match 2")

match = re.match(pattern, "! $?")
if match :
    print("Match 3")

# Soal 2 : Which pattern would NOT match "123!456!"?

# Jawaban 2 : (\D+\s?)+

# ================================================== #

# Materi 3 : Special Sequences #3
import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match :
    print("Match 1")

match = re.search(pattern, "We s>cat<tered")
if match :
    print("Match 2")

match = re.search(pattern, "We scattered")
if match :
    print("Match 3")

# Soal 3 : Which pattern would match 'SPAM!' in a search?

# Jawaban 3 : \AS...\b.\Z

# ================================================== #