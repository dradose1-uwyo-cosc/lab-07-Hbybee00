# Hayden Bybee
# UWYO COSC 1010
# 10/28/24
# Lab 07
# Lab Section: 16
# Sources, people worked with, help given to: 
# N/A

# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

factorial = 1

bound2 = input("Give a positive numeric value to find the factorial.")
number = 0

while bound2:
    if bound2.isdigit():
        break
    else:
        print("That isn't even a number, dawg. :(")
        bound2 = input("Enter a positive numeric value please.")

number = int(bound2)

for integer in range(1,number):
    if int(bound2) >= 0:
        if number > integer:
            factorial += factorial * integer
#this else statement isn't really necessary because a negative number isn't accepted in the while loop before, but I already typed it out so it's staying here
    else:
        print("Not a valid numerical value.")
        bound2 = input("A positive numerical value, please.")


print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 
Isneg = False


while True:
    numbers = input("What number should we add? 'exit' to stop adding.")
    if numbers.lower() == "exit":
        break
    else:
        str(numbers)
        for number in numbers:
            if number == "-":
                del number
                Isneg = True
            else:
                pass
            if numbers.isdigit():
                numbers = int(numbers)
                if Isneg == True:
                    num_sum += (numbers*-1)
                elif Isneg == False:
                    num_sum += numbers
            else: 
                print("That isn't a valid digit.")

print(f"Your final sum is {num_sum}")
#The negatives aren't negative-ing for some reason, I tried to make it work but I can't figure out how to fix it
print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

varuno = ""

while True:
    uncalculated = input("Please input something to calculate-- in operand operator operand format!")
    for unc in uncalculated:
        if unc == " ":
            del unc
        else:
            varuno += unc + " "
    uncalclist = varuno.split(" ")
    uncalc1 = uncalclist[0]
    uncalc2 = uncalclist[1]
    uncalc3 = uncalclist[2]
    if not uncalc1.isdigit():
        print("Invalid first operand.")
        pass
    elif not uncalc3.isdigit():
        print("Invalid second operand.")
        pass
    else:
        break

def calculator(operandone,operator,operandtwo):
    """This is a simple calculator that can use +, -, /, *, and %"""
    calculated = 0
    if operator == "+":
        calculated = int(operandone) + int(operandtwo)
        return calculated
    elif operator == "-":
        calculated = int(operandone) - int(operandtwo)
        return calculated
    elif operator == "*":
        calculated = int(operandone) * int(operandtwo)
        return calculated
    elif operator == "/":
        calculated = int(operandone) / int(operandtwo)
        return calculated
    elif operator == "%":
        calculated = int(operandone) % int(operandtwo)
        return calculated
    else:
        print("not valid calculation.")

print(calculator(uncalc1,uncalc2,uncalc3))

