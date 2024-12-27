# and(&) , or(||) , not(!) 

sum = int(input("Sum of ten numbers: "))

if(sum == 500):
    print("Sum of ten numbers is 500.")
elif(sum > 0 and sum <= 499):
    print("Sum of ten numbers is between 0 to 499.")
elif(sum > 500 or sum <= 1000):
    print("Sum of ten numbers is between 501 to 1000.")
else:
    print("Sum of ten numbers is infinity.")
    
    