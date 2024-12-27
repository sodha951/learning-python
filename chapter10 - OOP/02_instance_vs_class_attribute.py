class Employee:
    language = "Python" #class attribute
    salary = 12000000
    
harry = Employee()
harry.language = "JavaScript" #instance attribute
print(harry.language, harry.salary)

# Instance attributes,take preference over class attributes during assignment & retrivel