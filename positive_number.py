#Python program to print all positive numbers in a range.

myList = [15,5,-10,25,-30,20,-100,0]
for i in myList:
    if i<0:
        myList.remove(i)
print('New list: ',myList) #unsorted list
myList.sort()
print('New sorted list: ',myList) #sorted list
