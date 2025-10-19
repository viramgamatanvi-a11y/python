'''Types of Control Structure'''


'''1. Sequential Control Structure'''



# print("Hello!")  
# print("Welcome to Python.")  
# print("Enjoy coding!")  






'''
2. Selection Control Structure (Decision-Making)
(a) if Statement
(b) if-else Statement
(c) Ladder Statement
(d) Nested Statement
(e) Short-hand Syntax or Ternary Statement
'''






'''3. Looping Control Structure (Iteration)
(a) for Loop (Iterates Over a Sequence)
(b) while Loop (Runs Until Condition Becomes False)
(c) Loop Control Statements
'''





'''Working of if statement'''


# num = 10
# if num > 0: 
#     print("The number is positive.")  
# print("This statement always runs.")






# age = int(input("Enter your age: "))  
# if age >= 18:
#     print("You are eligible to vote.")
# print("Program ended.") 






# num = 8
# if num > 0 and num % 2 == 0: 
#     print(f"{num} is a positive even number.")






'''Working of if else statement'''


# num = int(input("Enter a number: ")) 
# if num % 2 == 0: 
#     print(f"{num} is an even number.")  
# else:
#     print(f"{num} is an odd number.")






# age = int(input("Enter your age: "))  
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")






# num = -5
# if num >= 0:
#     print("Positive Number")
# else:
#     print("Negative Number")






# text = input("Enter some text: ")
# if text:
#     print("You entered:", text)
# else:
#     print("You entered an empty string!")






# if 10>5:
#     print("Yes this is True")
# else:
#     print("Yes this is false")






# num1=int(input("Enter your 1 number : "))
# num2=int(input("Enter your 2 number : "))

# if num1>num2:
#     print("This is biggest")
# else:
#     print("This is loyest")







'''Working of if elif ... else (ladder) statement'''


# marks = int(input("Enter your marks: ")) 
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 50:
#     print("Grade: D")
# else:
#     print("Grade: F")







# day = int(input("Enter a number (1-7) for day of the week: "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day number")






# temp = 32

# if temp < 0:
#     print("It's freezing!")
# elif temp >= 0 and temp < 10:
#     print("It's cold!")
# elif temp >= 10 and temp < 20:
#     print("It's cool!")
# elif temp >= 20 and temp < 30:
#     print("It's warm!")
# else:
    # print("It's hot!")
    
    
    
    
    
    
    
# age = int(input("Enter your age: "))

# if age <= 12:
#     print("Child")
# elif age <= 19:
#     print("Teenager")
# elif age <= 35:
#     print("Adult")
# elif age <= 60:
#     print("Middle-aged")
# else:
#     print("Senior Citizen")






'''Working of nested if statements'''


# num = 15

# if num >= 10:
#     if num <= 20:
#         print(f"{num} is between 10 and 20")
#     else:
#         print(f"{num} is greater than 20")
# else:
#     print(f"{num} is less than 10")






# age = 18
# citizenship = "USA"

# if age >= 18:
#     if citizenship == "USA":
#         print("You are eligible to vote.")
#     else:
#         print("You are not a citizen.")
# else:
#     print("You are underage and cannot vote.")






# num = 12

# if num >= 0:
#     if num % 2 == 0:
#         print(f"{num} is an even number.")
#     else:
#         print(f"{num} is an odd number.")
# else:
#     print("The number is negative.")






# maths = 75
# english = 65
# science = 80

# if maths >= 50:
#     if english >= 50:
#         if science >= 50:
#             print("You passed all subjects.")
#         else:
#             print("You failed science.")
#     else:
#         print("You failed english.")
# else:
#     print("You failed maths.")







# a=int(input("Enter a num1: "))
# b=int(input("Enter a num2: "))
# c=int(input("Enter a num3: "))

# if a>b:
#     if a>c:
#         print("A is biggest")
#     else:
#         print("C is biggest")
        
# else:
#     if b>c:
#         print("B is biggest")
#     else:
#         print("C is biggest")







# a=int(input("Enter a number : "))

# if a>10:
#     if a%2==0:
#         print("A is greter than 10 and an even number")
#     else:
#         print("A is greter than 10 and an odd number")

# else:
#     print("A is less than")







'''Working of Short-hand syntax (Ternary Statement)'''


# num = 10
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)






# a = 15
# b = 20
# max_num = a if a > b else b
# print("Maximum number:", max_num)






# age = 18
# status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
# print(status)






# marks = 85
# grade = "A" if marks >= 90 else "B" if marks >= 70 else "C"
# print("Grade:", grade)






# num=44
# result="even" if num%2==0 else "odd"
# print(result)







'''match case in python'''


# day=2

# match day:
#     case 1:
#         print("Monday")
        
#     case 2:
#         print("Tuesday")
        
#     case _:
#         print("Invalid")
  
      