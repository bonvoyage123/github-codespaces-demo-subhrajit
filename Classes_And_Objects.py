print(f"Name / Occupation / Company")
class Person:
    name = "Subhrajit"
    occupation = "Data Engineer"
    company = "CBA"

    def info(self):
        print(f"{self.name} is a {self.occupation} in {self.company}")

a = Person()
b = Person()
c = Person()


a.name = "Uday"
a.occupation = "Sr.Data Engineer"
a.company = "TCS"

b.name = "Obed"
b.occupation = "Software Engineer"
b.company = "BOFA"


a.info()
b.info()

c.info()
