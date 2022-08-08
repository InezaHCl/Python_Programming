""" Write a program which repeatedly reads numbers until the user enters "done".Once done is Entered ,print out the total,count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number."""

count = 0
total = 0
list = [] #empty list

while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        num = int(value)
        list.append(num)
    except:
        print('Invalid input')
print(list)

for i in list:
    count = count + 1
    total = total + i
average = total / count   
print('count: ',count)
print('Total: ',total)
print('Average: ',average)
