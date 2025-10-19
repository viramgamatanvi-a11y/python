'''Function and it's Types'''


'''Types of Functions in Python'''


'''
 Built-in Functions : (Predefined functions like print(), len(), max(), etc.)
 User-defined Functions : (Custom functions created by the programmer)
'''



'''1. Built-in Functions'''


# print(len("Hello")) 
# print(max([3, 5, 9, 1]))  






'''2. User-defined Functions'''


# def greet(name):
#     print("Hello, " + name)

# greet("Alice") 






'''User Defined Function (UDF)'''


'''Types of User-Defined Functions'''


'''1. Function Without Parameters & Without Return (Take nothing return nothing) (tnrn)'''


# def greet():
#     print("Hello, World!")

# greet()







'''2. Function With Parameters & Without Return (Take something return nothing) (tsrn)'''


# def add(a, b):
#     print("Sum:", a + b)

# add(3, 5)







'''3. Function With Parameters & With Return (Take something return nothing) (tsrs)'''


# def multiply(a, b):
#     return a * b

# result = multiply(4, 5)
# print("Product:", result) 







'''4. Function Without Parameters & With Return (Take nothing return something) (tnrs)'''


# def get_pi():
#     return 3.1416

# pi_value = get_pi()
# print("Pi:", pi_value)







'''Types of Function Arguments'''


'''
1.Positional Arguments
2.Default Arguments
3.Keyword Arguments
4.Variable-Length Arguments (*args, **kwargs)
'''






'''1. Positional Arguments'''


# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Alice", 25)  







'''2. Default Arguments'''


# def greet(name, age=18):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Bob")  

# greet("Alice", 25)  








'''3. Keyword Arguments'''


# def student(name, subject):
#     print(f"{name} is studying {subject}.")

# student(name="John", subject="Math")  

# student(subject="Science", name="Emma")  







'''4. Variable-Length Arguments'''


'''A. *args (Non-Keyword Arguments - Tuple Format)'''


# def add_numbers(*args):
#     print("Sum:", sum(args))

# add_numbers(2, 4, 6)  







'''B. **kwargs (Keyword Arguments - Dictionary Format)'''


# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# show_info(name="Alice", age=25, city="NY")  







'''C. Using *args and **kwargs Together'''


# def display_data(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# display_data(1, 2, 3, name="Alice", age=25)







'''Document String'''


'''Types of Docstrings'''


'''1. Function Docstring'''


# def add(a, b):
#     """This function returns the sum of two numbers."""
#     return a + b

# print(add.__doc__)







'''2. Class Docstring'''


# class Student:
#     """This class represents a student with name and age."""
    
#     def __init__(self, name, age):
#         """Initializes the student's name and age."""
#         self.name = name
#         self.age = age

# print(Student.__doc__)  
# print(Student.__init__.__doc__) 







'''3. Module-Level Docstring'''


# """
# This module provides functions for basic arithmetic operations.
# """

# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b







'''4. Multi-Line Docstring'''


# def greet(name):
#     """
#     This function greets a person.

#     Parameters:
#         name (str): The name of the person.

#     Returns:
#         str: Greeting message.
#     """
#     return f"Hello, {name}!"

# print(greet.__doc__)








'''Recursion'''



# def factorial(n):
#     if n == 1:  
#         return 1
#     return n * factorial(n - 1)  

# print(factorial(5))







# def fibonacci(n):
#     if n <= 0:  
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)  
# print(fibonacci(6)) 







# def sum_natural(n):
#     if n == 1: 
#         return 1
#     return n + sum_natural(n - 1)  

# print(sum_natural(5))







''' Anonymous/Lambda Function'''


# add = lambda a, b: a + b

# print(add(5, 3))







# numbers = [1, 2, 3, 4, 5]

# doubled = list(map(lambda x: x * 2, numbers))

# print(doubled)  







# numbers = [1, 2, 3, 4, 5, 6]

# evens = list(filter(lambda x: x % 2 == 0, numbers))

# print(evens)  







# students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]

# sorted_students = sorted(students, key=lambda x: x[1])

# print(sorted_students)  







'''from functools import reduce'''


# numbers = [1, 2, 3, 4, 5]

# product = reduce(lambda x, y: x * y, numbers)

# print(product)  







'''global keyword'''


# x = 10  

# def my_function():
#     x = 5  
#     print("Inside function:", x)

# my_function()
# print("Outside function:", x)







# x = 10 

# def my_function():
#     global x  
#     x = 5  
#     print("Inside function:", x)

# my_function()
# print("Outside function:", x)







# a = 100
# b = 200

# def update_values():
#     global a, b
#     a += 10
#     b -= 20

# update_values()
# print(a, b)








# def outer():
#     global x
#     x = "Hello"

#     def inner():
#         global x
#         x = "World"

#     inner()
#     print("Inside outer:", x)

# outer()
# print("Outside function:", x)







'''Returning multiple values from a Function'''


'''Using Tuples (Default Way)'''


# def get_values():
#     return 10, 20, 30  
# result = get_values()
# print(result)







'''Using Lists'''


# def get_list():
#     return [1, 2, 3, 4]

# result = get_list()
# print(result) 






'''Using Dictionaries'''


# def get_student():
#     return {"name": "Alice", "age": 20, "grade": "A"}

# student = get_student()
# print(student["name"], student["age"])







'''Using Multiple Return Variables'''


# def get_numbers():
#     return 5, 10

# x, y = get_numbers()
# print(x, y)







'''Nested Function'''


# def greet(name):
#     def message():
#         return f"Hello, {name}!"
    
#     return message() 

# print(greet("Alice")) 







# def multiplier(factor):
#     def multiply(number):
#         return number * factor 
#     return multiply  
# double = multiplier(2) 
# print(double(5))







# def login(username, password):
#     def validate():
#         return username == "admin" and password == "1234"
    
#     if validate():
#         return "Login Successful!"
#     else:
#         return "Invalid Credentials!"

# print(login("admin", "1234"))






