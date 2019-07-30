# Declare variable and initialize it
f = 0
print(f)  # => 0

# Re-declaring the variable works
f = "abc"
print(f)  # => abc

# Error: variables of different types cannot be combined
# print ("abc" + 1) => error
print ("abc" + str(1))  # => abc1


# Global vs. local variables in functions
def function1():
    f = "def"
    print(f)  # => def


function1()
print(f)  # f values doesn't change => abc


def function2():
    global f
    f = "def"
    print(f)  # f values changed => def


function2()
print(f)  # f values changed => def

del f
# print(f) => error