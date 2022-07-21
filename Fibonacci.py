# program to dsiplay the fibonacci sequence up to n-th term

nterms = int(input("How many terms?: "))

#first two terms
n1 = 0
n2 = 1
count = 0
Sum = 0

#check if the number of terms is valid
if nterms <= 0:
    print("Please Enter a positive enteger!")
# if there is only one term, return n1
elif nterms == 1:
    print('Fibonacci sequence upto',nterms,':')
    print(n1)
#General fibonacci sequence 
else:
    print('fibonacci sequence:')
    while count < nterms:
        print(n1)
        Sum = n1 + n2
        #update values
        n1 = n2
        n2 = Sum
        count = count +1
