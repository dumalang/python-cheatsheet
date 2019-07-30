# define a basic function
def func1():
    print("I am a  function")


# func1()
# print(func1())
# print(func1)  # func1 is an objects


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# func2(10, 20)
# print(func2(10, 20))
# print(func2)


# function that returns a value
def cube(x):
    return x * x * x


print(cube(3))


# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


print(power(3))
print(power(3, 3))
print(power(x=2, num=5))


# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(10,10,11))