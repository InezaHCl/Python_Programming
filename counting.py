"""
Python program to counts the number of times the letter appears in a string using loop function
"""

#counting how many times the letter "a" appears in a string

word = "banana"
count = 0  #The variable count is initialized to 0
for letter in word:
    if letter == 'a':
        count = count + 1  # the variable count is incremented each time an "a" is found
print(count)  #When the loop exits, count contains the results
