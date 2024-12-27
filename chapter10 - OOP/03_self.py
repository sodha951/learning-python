class Employee:
    language = "Python" #class attribute
    salary = 12000000
    
    # self refers to the instance of the class. it is automatically passed with a function call from an object.
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")
        
    @staticmethod
    def greet():
        print("Good morning")
    
harry = Employee()
harry.language = "JavaScript" #instance attribute
# harry.getInfo()
Employee.getInfo(harry)
harry.greet()
# Employee.greet(harry)