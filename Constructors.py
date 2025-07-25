class Person:
    def __init__(self,n,o,c):
        self.name = n
        self.occupation = o
        self.company = c

    def info(self):
        print(f"{self.name} is a {self.occupation} in {self.company}")

try:
    a = Person("Uday","Sr.Data Engineer","TCS")
    b = Person("Obed","Software Engineer","BOFA")
    c = Person("Rajesh","Assoc.Data Engineer","CBA")

    a.info()
    b.info()
    c.info()

except e:
    print ("Parameters for some user is incomplete or not provided")