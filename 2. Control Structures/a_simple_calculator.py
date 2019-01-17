# ================================================== #

# Materi 1 : Creating a Calculator #1
# while True :
#     print("Options : ")
#     print("Enter 'add' to add two numbers")
#     print("Enter 'subtract' to subtract two numbers")
#     print("Enter 'multiply to multiply two numbers")
#     print("Enter 'divide' to divide two number")
#     print("Enter 'quit' to end the program")
#     user_input = input(": ")

#     if user_input == "quit" :
#         break
#     elif user_input == "add" :
#         ...    
#     elif user_input == "subtract" :
#         ...
#     elif user_input == "multiply" :
#         ...
#     elif user_input == "divide" :
#         ...
#     else :
#         print("Unknown input")

# Soal 1 : If we were to replace the break statement in the code with a 'continue', what would happen?

# Jawaban 1 : It would run forever

# ================================================== #

# Materi 2 : Creating a Calculator #2
# elif user_input == "add" :
#     num1 = float(input("Enter a number : "))
#     num2 = float(input("Enter another number : "))

# Soal 2 : Why are the calls to float necessary in the code?

# Jawaban 2 : To convert user input to a float

# ================================================== #

# Materi 3 : Creating a Calculator #3
# elif user_input == "add" :
#     num1 = float(input("Enter a number : "))
#     num2 = float(input("Enter another number : "))
#     result = str(num1 + num2)
#     print("The answer is " + result)

# Soal 3 : Fill in the blanks to make the calculator work for multiplication.
# elif user_input == "multiply" :
#     num1 = float(input("Enter a number : "))
#     num2 = _____(input("Enter another number : "))
#     result = str(num1 _ num2)
#     print("The answer is " + ______)

# Jawaban 3 :
# elif user_input == "multiply" :
#     num1 = float(input("Enter a number : "))
#     num2 = float(input("Enter another number : "))
#     result = str(num1 * num2)
#     print("The answer is " + result)

# ================================================== #

while True :
    print("Options : ")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply to multiply two numbers")
    print("Enter 'divide' to divide two number")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit" :
        break
    elif user_input == "add" :
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = str(num1 + num2)
        print("The answer is " + result)    
    elif user_input == "subtract" :
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = str(num1 - num2)
        print("The answer is " + result)    
    elif user_input == "multiply" :
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = str(num1 * num2)
        print("The answer is " + result)    
    elif user_input == "divide" :
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = str(num1 / num2)
        print("The answer is " + result)    
    else :
        print("Unknown input")

# ================================================== #