# Problem4: Write a program to find whether a given number is prime or not.

# num = int(input("Enter a number: "))

# for i in range(2, num):
#     if(num % 2 == 0):
#         print("Number is not prime")
#         break
#     else:
#         print("Number is prime")
        
n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
