# ================================================== #

# Materi 1 : List Operations #1
nums = [7,7,7,7,7]
nums[2] = 5
print(nums) # [7,7,5,7,7]

# Soal 1 : What is the result of this code?
nums = [1,2,3,4,5]
nums[3] = nums[1]
print(nums[3])

# Jawaban 1 : 2

# ================================================== #

# Materi 2 : List Operations #2
nums = [1,2,3]
print(nums + [4,5,6]) # [1,2,3,4,5,6]
print(nums * 3) # [1,2,3,1,2,3,1,2,3]

# Soal 2 : Fill in the blanks to create a list, reassign its 2nd element and print the whole list.
# nums = [33,42,56_
# nums[_] = 22
# print(____)

# Jawaban 2 : 
nums = [33,42,56]
nums[1] = 22
print(nums)

# ================================================== #

# Materi 3 : List Operations #3
words = ["spam","egg","spam","sausage"]
print("spam" in words) # True
print("egg" in words) # True
print("tomato" in words) # False

# Soal 3 : What is the result of this code?
nums = [10,9,8,7,6,5]
nums[0] = nums[1] - 5
if 4 in nums :
    print(nums[3])
else :
    print(nums[4])

# Jawaban 3 : 7

# ================================================== #

# Materi 4 : List Operations #4
nums = [1,2,3]
print(not 4 in nums) # True
print(4 not in nums) # True
print(not 3 in nums) # False
print(3 not in nums) # False

# Soal 4 : Fill in the blanks to print "Yes" if the list contains 'z':
# letters = ['a','b','z']
# _ "z" __ letters :
#   print("Yes")

# Jawaban 4 :
letters = ['a','b','c']
if "z" in letters :
    print("Yes")

# ================================================== #