'''Types of Loops'''


'''
for loop
while loop
Nested loop
'''



'''1. for Loop'''


# for i in range(1, 6):
#     print(i)





'''2. while Loop'''


# i = 1
# while i <= 5:
#     print(i)
#     i += 1 





'''3. Nested Loop'''


# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}")






'''Working of while loop'''


# i = 1  
# while i <= 5:  
#     print(i)  
#     i += 1  






# sum = 0
# num = 1

# while num <= 10:
#     sum += num  
#     num += 1  

# print("The sum of numbers from 1 to 10 is:", sum)






# correct_number = 7
# guess = None

# while guess != correct_number:
#     guess = int(input("Guess the number (between 1 and 10): "))
#     if guess < correct_number:
#         print("Too low!")
#     elif guess > correct_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You've guessed the correct number!")







# while True: 
#     user_input = input("Type 'exit' to stop: ")
#     if user_input == "exit":
#         print("Exiting the loop...")
#         break 
#     else:
#         print("Keep typing...")







'''range() function'''


# for i in range(5):
#     print(i)






# for i in range(2, 6):
#     print(i)






# for i in range(1, 11, 2):
#     print(i)






# for i in range(10, 0, -1):
#     print(i)






# numbers = list(range(1, 6))
# print(numbers)







# for i in range(10, 0, -2):
#     print(i)






# for i in range(5,15):
#     print(i)






# for i in range (5,15,2):
#     print(i)







# num=int(input("Enter a number to print table : "))

# for i in range (1,11):
#     print(num,"x",i,"=",num*i)






# for i in range(5):
#     print("* * * * * ")






# for i in range(5):
#     print("* "*5)






# for i in range(1,6):
#     print("i "*i)






# for i in range(5):
#     print(str(i)*5)
    
    
    
    
    


# for i in range(1,6):
#     print(str(i)*i)






# for i in range(1,6):
#     for j in range(1,i):
#         print(j,end=" ")
#     print("\n")






# for i in range(5,1,-1):
#     print("* "*i)
    
    
    
    
    
    
# for i in range(5,0,-1):
#     print(str(i)*i)  






# for i in range (15,5,-1):
#     print(i)






''' Working of for loop'''


# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)






# word = "Python"
# for char in word:
#     print(char)






# for i in range(1, 6):  
#     print(i)






# student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
# for student, score in student_scores.items():
#     print(f"{student}: {score}")






'''List Comprehension'''


# squares = [x**2 for x in range(5)]
# print(squares)






# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)






# even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares)






# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = [item for sublist in matrix for item in sublist]
# print(flat_list)






# words = ["apple", "banana", "cherry"]
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)






# input_string = "Hello World"
# vowels = "aeiou"
# no_vowels = [char for char in input_string if char.lower() not in vowels]
# print("".join(no_vowels))






'''Control Statements'''


''' 1. break Statement'''


# for i in range(10):
#     if i > 5:
#         break
#     print(i)







'''2. continue Statement'''


# for i in range(10):
#     if i % 2 == 0:
#         continue  
#     print(i)






''' 3. pass Statement'''



# def placeholder_function():
#     pass  
# placeholder_function()







'''Example 4: Using break, continue, and pass Together'''



# for i in range(10):
#     if i == 3:
#         pass  
#     elif i == 5:
#         continue  
#     elif i == 8:
#         break  
#     print(i)






'''Nested Loop'''


# for i in range(5): 
#     for j in range(5):  
#         print("*", end=" ")
#     print()  






# for i in range(1, 6):  
#     for j in range(i): 
#         print("*", end=" ")
#     print()






# for i in range(1, 6): 
#     for j in range(1, 6):  
#         print(i * j, end="\t") 
#     print()






# i = 1
# while i <= 3: 
#     j = 1
#     while j <= 3:
#         print(i * j, end=" ")
#         j += 1
#     print()
#     i += 1






# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:  
#     for num in row:  
#         print(num, end=" ")
#     print()



