print ("Running Getters and Setters")

class MyClass:
    def __init__ (self, value):
        self._value = value

    def show (self):
        print (f"Value passed is: {self._value}")

    @property
    def ten_x_value (self):
        return 10*self._value

    @ten_x_value.setter
    def ten_x_value (self,new_value):
        self._value = new_value

obj = MyClass (19999999999)
obj.show()
#print (f"10X value is: {obj.ten_x_value}")

obj.ten_x_value = 60
obj.show()
print (f"10X value is: {obj.ten_x_value}")