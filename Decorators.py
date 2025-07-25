def decorator (fx):
    #Defining a decorator function named decorator.
    # It takes a function fx as its argument — this is the function being decorated (like hello or add).

    def mfx(*args):
        # Inside the decorator, we're defining an inner function called mfx.
        # It accepts any number of positional arguments (*args) and keyword arguments (**kwargs).
        # This makes the decorator flexible enough to handle any function signature.

        print ("Good Morning !!")
        # This line runs before the actual function fx() is called.

        fx(*args)
        # This is where the actual decorated function (like hello() or add(a, b)) is called

        # We’re passing along any arguments the original function expects.
        # If it's hello(), args is empty — works fine.
        # If it's add(3, 6), args becomes (3, 6) — also handled correctly.

        print ("Thanks for using the function")
        print ("-----------------------------")
        #These lines run after the decorated function finishes.
        # Acts like a post-processing message or footer.

    return mfx
    # We're returning the inner function itself.
    # This is what enables @decorator to replace hello or add with the modified version. (IMP)

@decorator
def hello ():
    print ("Hello World !!")
# Syntactic sugar in Python. Equivalent to: hello = decorator(hello)
# When we call hello(), you're actually calling mfx() with no arguments.

@decorator
def add (a,b):
    print (a+b)
# When we later call add(3, 6), it goes through the decorator wrapper mfx, prints greetings, calls the real add(a, b), then prints the footer.

hello ()
add (3,6)
# Function calls that now include extra behavior thanks to the decorator.
