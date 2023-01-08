"""Write a Python Program to Illustrate Different Set Operations.
Here we have to define two set variables and we have to perform different set operations: 
union, intersection, difference and symmetric difference.
Your Output should look something like this
Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8} Intersection of E and N is {2, 4} Difference of E and N is {8, 0, 6} 
Symmetric difference of E and N is {0, 1, 3, 5, 6, 8)"""

#declaring the two sets E and N
E = {1,2,3,4,5}
N = {0,2,4,6,8}

#intersection of E an N
print('Union of E and N is: ',E.union(N))
#Intersection of E and N
print('Intersection of E and N is: ',E.intersection(N))
#Difference of E and N
print('Difference of E and N is: ',N.difference(E))
#Symmetric difference of E and N
print('Symmetric difference of E and N is: ',N.symmetric_difference(E))
