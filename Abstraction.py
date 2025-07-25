class MyClass:
    def __init__ (self,n,a):
        self.name = n
        self.__age = a

    def info (self):
        print (self.name)
        print (self.__age)
        """This will give an Attribute error. Here we are trying to access "age" which is not present anywhere in the class.
        If we use "__age"", that will not trigger an error """

p1 = MyClass("Subhrajit",35)
print ("Accessing Variables through Method")
p1.info()

print ("Accessing Variables through instances")
print (p1.name)
#print (p1.__age)
"""AttributeError: 'MyClass' object has no attribute '__age'. This is because self.__age in the constructor is stored as p1._MyClass__age, not as p1.__age.
This is called name mangling"""
print (p1._MyClass__age)  # name mangling :: Not a recommended approach, doesn't solve the purpose of privacy
"""name mangling :: object._class__private variable.
When we initialize, self.__age, Python internally changes the attribute’s name to _MyClass__age"""