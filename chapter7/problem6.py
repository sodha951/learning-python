# Problem6 : Write a progrma to calculate the factorial of a given number using for loop

n = int(input("Enter the number: "))
product = 1

for i in range(1, n+1):
    product = product * i
    
print(f"The factorial of {n} is {product}")