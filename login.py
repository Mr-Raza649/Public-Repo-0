
# def func():
#     print("This is login file code")
    
# func()

# def my_function(fname):
#     print(fname +  " Login")
    
# my_function("Gmail")

# def exFun(fname, lname = "John"):
#     print(fname + " " + lname)
    
# exFun("John", "Carter")
# exFun("Jasper")

# def keyArgFun(fname, lname):
#     print(fname + " " + lname)

# keyArgFun(lname = "Smith", fname = "Will")

# def myfunc(fruit):
#     for x in fruit:
#         print(x)
        
# fruits = ["apple", "banana", "cherry", "Orange"]
# myfunc(fruits)


numbers = [21, 20, 3, 4, 5, 77, 8, 11]

def fun(number):
    return number % 2 == 0

even_numbers = filter(fun, numbers)

# lambda is an anonymous function that can take any number of arguments but can only have one expression. It is often used for short, simple functions that are not reused elsewhere in the code.
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print(list(even_numbers))
print(list(odd_numbers))

# , / allows us to specify that the parameters before / are positional-only parameters, which means they must be passed positionally and cannot be used as keyword arguments.

def mfn(fname, lname, /):
    print(fname + " " + lname)
    
mfn("John", "Smith")

# *, allows us to specify that the parameters after * are keyword-only parameters, which means they must be passed as keyword arguments and cannot be used as positional arguments.

def fn(*, fname, lname):
    print(fname + " " + lname)
    
fn(fname = "John", lname = "Carter")
