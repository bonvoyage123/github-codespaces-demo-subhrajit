# How does a recursive function work ?

def factorial (a):
    if (a==0 or a==1):
        return 1
    else:
        return a * factorial (a -1)

def fibo (y):
    if y==1:
        return 1
    elif y==0:
        return 0
    else:
        a = 0
        print (a)
        b = 1
        print (b)
        for i in range (y):
           c= a+b
           print (c, sep = ',')
           a=b
           b=c

# Below is the exception handling
try:
    c = int (input ("Enter a number :"))
    j = factorial(c)
    print (f"Factorial of {c} is: {j}")
    e = fibo(c)
    #print (f"Fibonacci series until {c} is: {e}")

except:  #Exception as e:
    #print (e)
    print ("Invalid Input")
print ("thanks")


