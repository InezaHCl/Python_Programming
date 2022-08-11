""" Program That repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the numbers entered
and prints out both maximum and minimum of the numbers. """

list = []   #creating an empty list, where numbers will be stored

while True:
    val = input('Enter a number: ')
    if val == 'done':
        break
#Because user can enters anything other than a number, i am using "Try and except" print an error message and skip to the next number
    try:
        num = int(val)
        list.append(num)
    except:
        print('Invalid input')
print(list)

#find the largest number in list
largest = None
for i in list:
    if largest is None or i>largest:
        largest = i
print('Largest: ',largest)

#find the smallest  number in list
smallest = None
for i in list:
    if smallest is None or i< smallest:
        smallest = i
print('Smallest: ',smallest)
