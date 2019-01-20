# ================================================== #

# Materi 1 : Object Lifecycle #1
# Creation
# Manipulation
# Destruction
# Instantiation

# Soal 1 : Which stage corresponds to the __init__ method being called?

# Jawaban 1 : instantiation

# ================================================== #

# Materi 2 : Object Lifecycle #2
a = 42 # Create object <42>
b = a # Increase ref. count of <42>
c = [a] # Increase ref. count of <42>

del a # Decrease ref. count of <42>
b = 100 # Decrease ref.count of <42>
c[0] = -1 # Decrease ref. count of <42>

# Soal 2 : What is __del__ the magic method for?

# Jawaban 2 : del instance

# ================================================== #