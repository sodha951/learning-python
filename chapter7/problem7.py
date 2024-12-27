# Problem7 : Write a program to print the following star pattern.

 # '''  *
 #     ***
 #    ***** ''' for n = 3
 
n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" "* (n-i), end="") # for spaces n=3 i range from 1 to n start i = 1
    print("*"* (2*i-1), end="") # for print star
    print("") # for next line

