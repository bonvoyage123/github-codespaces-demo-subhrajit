class Employee :
    def __init__(self,name, id):
        self.name = name
        self.id = id

    def show (self):
        print (f"The Employee with {self.id} is {self.name}")

class Business_Analyst (Employee):   # Inheriting the main class "Employee"
    def showBA(self):
        print (f"{self.name} knows Python")

class HR (Employee):
    def showHR(self):
        print (f"{self.name} knows Resource Management")

class Programmer (Business_Analyst): #Inheriting the child class "Business_Analyst"
    def showProgrammer(self):
        print (f"Along with Python, {self.name} also has experience in AWS ")

e1 = Business_Analyst ("Subhrajit",481560)
e1.show()
e1.showBA()
print ("==========================")
print ()
e2 = Business_Analyst ("Udita",560876)
e2.show()
e2.showBA()
print ("==========================")
print ()
e2 = HR ("Udita",560876)
e2.show()
e2.showHR()
print ("==========================")
print ()
e3 = Programmer ("Uday",499975)
e3.show()
e3.showProgrammer()