
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


# 

# lambda is an anonymous function that can take any number of arguments but can only have one expression. It is often used for short, simple functions that are not reused elsewhere in the code.
# odd_numbers = filter(lambda x: x % 2 != 0, numbers)

# print(list(even_numbers))
# print(list(odd_numbers))

# , / allows us to specify that the parameters before / are positional-only parameters, which means they must be passed positionally and cannot be used as keyword arguments.

# def mfn(fname, lname, /):
#     print(fname + " " + lname)
    
# mfn("John", "Smith")

# *, allows us to specify that the parameters after * are keyword-only parameters, which means they must be passed as keyword arguments and cannot be used as positional arguments.

# def fn(*, fname, lname):
#     print(fname + " " + lname)
    
# fn(fname = "John", lname = "Carter")


# def ex_fun(fname, lname, /, age, *, city, country):
#     print(fname + " " + lname + " is " + str(age) + " years old and lives in " + city)
    
# ex_fun("John", "Smith", 30, city = "New York", country = "USA")

# def my_function(*args):
#     for arg in args:
#         print(arg)
        
# my_function("Hello", "Emaan", "Aavya", "Hable", "Test")

# def func(**kwargs):
#     for key, value in kwargs.items():
#         print(key + ": " + value)
        
# func(name = "John", age = "30", city = "New York")

# def f(*number):
#     if len(number) == 0:
#         print("No numbers provided")
#         return None
#     else:
#         max_num = number[0]
#         for num in number:
#             if num > max_num:
#                 max_num = num
#         return max_num  # Return after checking all numbers

# max_n = f(3, 5, 2, 8, 1)
# print(max_n)  # Output: 8

def max_value(number):
    if len(number) == 0:
        print("No numbers provided")
        return None
    else:
        max_num = number[0]
        for num in number:
            if num > max_num:
                max_num = num
        return max_num
            
numbs = [1, 3, 5, 8, 9, 4, 11, 1]

max_n = max_value(numbs)
print(max_n)            
