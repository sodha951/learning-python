# Problem10: Write a program to print multiplication table of n using for loops in reversed order.


n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n * (11-i)} ")