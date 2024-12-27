# Problem5 : Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number: "))
sum_natural_numbers = 0
i = 1

while (i <= n):
    sum_natural_numbers += i
    i += 1

print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers}")


n = int(input("Enter a number: "))

sum_natural_numbers = 0

for i in range(1, n + 1):
    sum_natural_numbers += i

print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers}")