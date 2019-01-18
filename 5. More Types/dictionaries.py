# ================================================== #

# Materi 1 : Dictionaries #1
ages = {"Dave":24,"Mary":42,"John":58}
print(ages["Dave"]) # 24
print(ages["Mary"]) # 42

# Soal 1 : Fill in the blanks to define a valid dictionary with two elements.
# cars = {"BMW"_"blue"_"Volvo":"red"_

# Jawaban 1 :
cars = {"BMW":"blue","Volvo":"red"}

# ================================================== #

# Materi 2 : Dictionaries #2
primary = {
    "red":[255,0,0],
    "green":[0,255,0],
    "blue":[0,0,255],
}

print(primary["red"]) # [255,0,0]
# print(primary["yellow"]) # KeyError: 'yellow'

# Soal 2 : What is the result of this code?
# test = {}
# print(test[0])

# Jawaban 2 : KeyError

# ================================================== #

# Materi 3 : Dictionaries #3
# bad_dict = {
#     [1,2,3]:"one two three",
# }

# TypeError: unhashable type: 'list'

# Soal 3 : Which of these values can't be used as a dictionary key?

# Jawaban 3 : {2:4,3:9,4:16,}

# ================================================== #