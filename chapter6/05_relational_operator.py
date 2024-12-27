# == , >= , <=

number = int(input("Enter your number: "))

if(number == 10):
    print("Number is equal to 10.")
elif(number >= 11 and number <= 100):
    print("Number is greater than or equal to 11.")
elif(number >= 0 and number <= 9):
    print("Number is less than or equal to 9.")
else:
    print("Enter valid number.")