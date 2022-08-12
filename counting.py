"""
Python program to counts the number of times the letter appears in a string using loop function
"""

#counting how many times the letter "a" appears in a string
def count(Str):
    val = input('Enter a letter you want to count: ')
    count = 0  #The variable count is initialized to 0
    for letter in Str:
        if letter == val:
            count = count + 1  #The variable count is incremented each time the letter you want is found
    return count  #The return statement send back the the computed value back to the calling code

Str = input('Enter a string: ')  #Asking the user to input the string
count(Str) #function call
