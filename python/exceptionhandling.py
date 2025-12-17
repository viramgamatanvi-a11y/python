'''Exception Handling'''

'''try … except'''

# try:
#     x = 10 / 0  
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
    



'''try … except … else'''

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print("Division successful! Result:", result)
    




'''try … except … finally'''

# try:
#     file = open("test.txt", "r")  
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     print("Execution completed.")





'''try … except … else … finally'''

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print("Success! Result:", result)
# finally:
#     print("Execution completed.")





'''raise and assert keywords'''

'''raise Keyword'''

'''Example 1: Raising a Custom Exception'''

# age = int(input("Enter your age: "))

# if age < 18:
#     raise ValueError("You must be at least 18 years old.")
# else:
#     print("Access granted!")






''' Example 2: Raising Different Exceptions'''

# def withdraw(amount):
#     if amount < 0:
#         raise ValueError("Amount cannot be negative!")
#     elif amount > 10000:
#         raise Exception("Withdrawal limit exceeded!")
#     else:
#         print(f"Withdrawal successful: ₹{amount}")

# withdraw(-500)





'''assert Keyword'''

'''Example 1: Basic Assertion'''

# num = int(input("Enter a positive number: "))

# assert num > 0, "Number must be positive!"

# print("Valid number:", num)






'''Example 2: Using assert in Functions'''

# def divide(a, b):
#     assert b != 0, "Denominator cannot be zero!"
#     return a / b

# print(divide(10, 2)) 
# print(divide(10, 0))





'''Custom Exception'''

'''Example 1: Creating & Raising a Custom Exception'''

# class AgeTooYoungError(Exception): 
#     def __init__(self, age):
#         super().__init__(f"Age {age} is too young! Minimum age is 18.")


# age = int(input("Enter your age: "))

# if age < 18:
#     raise AgeTooYoungError(age)  
# else:
#     print("Access granted!")





'''Example 2: Handling a Custom Exception with try-except'''

# class InsufficientBalanceError(Exception):
#     def __init__(self, balance, withdraw):
#         super().__init__(f"Insufficient balance! Available: ₹{balance}, Requested: ₹{withdraw}")

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientBalanceError(balance, amount)
#     balance -= amount
#     print(f"Withdrawal successful! Remaining balance: ₹{balance}")

# try:
#     withdraw(1000, 1500)  
# except InsufficientBalanceError as e:
#     print("Error:", e)






