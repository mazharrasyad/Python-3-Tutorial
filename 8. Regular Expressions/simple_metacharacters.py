# ================================================== #

# Materi 1 : Metacharacters #1
# Backslash \

# Soal 1 : Fill in the blanks to create a raw string.
# str = _"I am \r\a\w!"

# Jawaban 1 :
str = r"I am \r\a\w!"

# ================================================== #

# Materi 2 : Metacharacters #2
import re

pattern = r"gr.y"

if re.match(pattern, "grey") :
    print("Match 1")

if re.match(pattern, "gray") :
    print("Match 2")

if re.match(pattern, "blue") :
    print("Match 3")

# Soal 2 : What would '....' match?

# Jawaban 2 : Any four character string with no newlines

# ================================================== #

# Materi 3 : Metacharacters #3
import re

pattern = r"^gr.y$"

if re.match(pattern, "grey") :
    print("Match 1")

if re.match(pattern, "gray") :
    print("Match 2")

if re.match(pattern, "stingray") :
    print("Match 3")

# Soal 3 : Fill in the blanks to create a pattern that matches strings that contain 3 characters, out of which the last character is an exclamation mark.
# r"___$"

# Jawaban 3 : r"..!$"

# ================================================== #