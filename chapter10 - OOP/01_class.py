class Employee:
    language = "Py" #class attribute
    salary = 12000000
    
harry = Employee()
harry.name = "Harry" #instance attribute
print(harry.name,harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan ro robinson"
print(rohan.name,rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class