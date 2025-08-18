print ("This will show, how the if __name__ == __main__: works")

def geometric_mean(a,b):
    mean = (a * b) / (a + b)
    print("Geometric Mean is: ", mean)


def is_greater_number(a,b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater")



print(__name__)
if __name__ == "__main__":
    c = int(input("Enter 1st Number :"))
    d = int(input("Enter 2nd Number :"))
    geometric_mean(c,d)
    is_greater_number(c,d)

