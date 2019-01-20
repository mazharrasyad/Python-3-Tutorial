# ================================================== #

# Materi 1 : Email Extraction #1
str = "Please contact info@sololearn.com for assistance"

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

# Soal 1 : Which of these must be done with regular expressions, rather than string methods?

# Jawaban 1 : Checking to see if a string contains a date

# ================================================== #

# Materi 2 : Email Extraction #2
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match :
    print(match.group())

# Soal 2 : In our example, why is the dot character preceded by a backslash?

# Jawaban 2 : to treat it as a character

# ================================================== #