# Collection Data types

# str(String)
# list 
# tuple
# set 
# dict (dictionary)


# name = "Python"      
# array = [4, 7, 1, 9]     
# values = (3, 6, 9, 1, 4)  
# fruits = {"apple", "banana", "cherry"}  
# contacts = {"electrician": 458956, "plumber": 785623, "mechanic": 562378}  

# print(name)
# print(array)
# print(values)
# print(fruits)
# print(contacts)



# String Operations

# str1 = "Hello"
# str2 = "World"
# combined = str1 + " " + str2
# print(combined)


# repeated = "Ha" * 3 
# print(repeated)


# text = "Python"
# first_char = text[0]  
# last_char = text[-1]
# print(first_char)
# print(last_char)


# text = "Python"
# substring = text[1:4]
# print(substring)


# text = "Python"
# length = len(text)
# print(length)



# String Methods

# text = "Hello World"
# print(text.lower())


# text = "Hello World"
# print(text.upper())  


# text = "hello world"
# print(text.title())


# text = "hello world"
# print(text.capitalize()) 


# text = "   Hello World   "
# print(text.strip())


# text = "Hello World"
# print(text.split())  


# words = ['Hello', 'World']
# print(' '.join(words))



# text = "Hello World"
# print(text.find("World")) 



# text = "Hello World"
# print(text.replace("World", "Python")) 



# String formatting


# 1. Using the % Operator
# name = "Alice"
# age = 30
# formatted_string = "My name is %s and I am %d years old." % (name, age)
# print(formatted_string)


# 2. Using str.format() Method
# name = "Alice"
# age = 30
# formatted_string = "My name is {} and I am {} years old.".format(name, age)
# print(formatted_string)


# 3. Using f-Strings (Literal String Interpolation)
# name = "Alice"
# age = 30
# formatted_string = f"My name is {name} and I am {age} years old."
# print(formatted_string)


# 4. Using Template Strings
# from string import Template
# name = "Alice"
# age = 30
# template = Template("My name is $name and I am $age years old.")
# formatted_string = template.substitute(name=name, age=age)
# print(formatted_string)


# 5. Using str.center() Method

# Basic Example: Centering with Default Spaces

# s = "hello"
# centered = s.center(10)  
# print(f"'{centered}'")



# Centering with a Custom Fill Character

# s = "Python"
# centered = s.center(20, '*') 
# print(f"'{centered}'")



# Centering with Insufficient Width
# s = "hello, world!"
# centered = s.center(5)  
# print(f"'{centered}'")



# Using center() in String Formatting
# header = "Name"
# value = "Alice"
# formatted = f"{header.center(10)} | {value.center(10)}"
# print(formatted)




# String manipulation

# String Concatenation

# greeting = "Hello"
# name = "Alice"
# combined_string = greeting + ", " + name + "!"
# print(combined_string)


# String Formatting

# name = "Alice"
# age = 30
# formatted_string = f"{name} is {age} years old."
# print(formatted_string)


# name = "Alice"
# age = 30
# formatted_string = "{} is {} years old.".format(name, age)
# print(formatted_string)


# name = "Alice"
# age = 30
# formatted_string = "%s is %d years old." % (name, age)
# print(formatted_string) 


# Accessing Characters

# string1 = 'Hello, World!'
# first_character = string1[0]
# last_character = string1[-1]
# print(first_character)  
# print(last_character)


# String Slicing


# Basic Slicing

# text = "Hello, World!"
# substring1 = text[0:5]
# print(substring1) 
# substring2 = text[7:12]
# print(substring2) 


# Using Step

# text = "Hello, World!"
# substring3 = text[0:13:2]
# print(substring3)


# Negative Indexing

# text = "Hello, World!"
# substring4 = text[-6:-1]
# print(substring4)  
# substring5 = text[-5:]
# print(substring5)  



# Omitting Indices

# text = "Hello, World!"
# substring6 = text[:5]
# print(substring6) 
# name = "Python"
# substring7 = name[:]
# substring8 = name[::]
# substring9 = name[0::]
# substring10 = name[::1]
# substring11 = name[0::1]
# substring12 = name[0:len(name):1]
# print(substring7)   
# print(substring8)   
# print(substring9)   
# print(substring10)  
# print(substring11)  
# print(substring12)  



# 1. Shallow Copy (Copies Values)

# original_list = [1, 2, 3, 4, 5, 6]
# shallow_copy = original_list.copy()
# shallow_copy[0] = 100
# print("Original List:", original_list) 
# print("Shallow Copy:", shallow_copy)



# 2. Deep Copy (Copies Everything)

# original_list = [1, 2, 3, 4, 5, 6]
# deep_copy = original_list
# deep_copy[0] = 100
# print("Original List:", original_list)  
# print("Shallow Copy:", deep_copy) 


