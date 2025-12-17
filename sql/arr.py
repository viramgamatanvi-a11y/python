'''Array and it's Types'''


'''Types of Arrays Using Lists'''

'''One-Dimensional Array (1D List)'''


# arr = [10, 20, 30, 40, 50]  
# print(arr[2]) 





'''Multi-Dimensional Array (Nested List)'''


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[1][2])





'''Jagged Array (List of Lists with Different Lengths)'''


# jagged = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 7, 8, 9]
# ]
# print(jagged[2][1])





'''Dynamic Array (Modifiable List)'''


# arr = [10, 20, 30]
# arr.append(40)  
# arr.remove(20)
# print(arr) 





'''1D Array'''


'''What is a 1D Array?'''


# arr = [10, 20, 30, 40, 50]  
# print(arr) 





# arr = [10, 20, 30, 40, 50]

# print(arr[0])   
# print(arr[2])  
# print(arr[-1])





'''Negative indexing starts from the end (-1 is the last element).'''


'''Slicing (Extracting a Subarray)'''


# arr = [10, 20, 30, 40, 50, 60, 70]

# print(arr[1:4])  
# print(arr[:3])    
# print(arr[2:])   
# print(arr[::2])  
# print(arr[::-1]) 





'''CRUD Operations on 1D Array'''


'''Create (Adding Elements)'''


# arr = [] 
# arr.append(10)  
# arr.append(20)
# arr.append(30)
# print(arr) 





# arr = []
# arr.insert(1, 15)  
# print(arr)  

# arr.extend([40, 50]) 
# print(arr)





'''Read (Accessing Elements)'''


# arr = [10, 20, 30, 40, 50, 60, 70]
# print(arr[2]) 





# arr = [10, 20, 30, 40, 50, 60, 70]
# print(arr[0:3])





# arr = [10, 20, 30, 40, 50, 60, 70]
# for elem in arr:
#   print(elem)





'''Update (Modifying Elements)'''


# arr = [10, 20, 30, 40, 50, 60, 70]
# arr[1] = 25  
# print(arr) 





'''Delete (Removing Elements)'''


# arr = [10, 20, 30, 40, 50, 60, 70]

# arr.pop(2)  
# print(arr)





# arr = [10, 20, 30, 40, 50, 60, 70]

# arr.remove(40)  
# print(arr) 





# arr = [10, 20, 30, 40, 50, 60, 70]

# del arr[1]  
# print(arr) 





# arr = [10, 20, 30, 40, 50, 60, 70]
# arr.clear()  
# print(arr)





'''Sorting'''


'''Sorting Using sort() (In-Place)'''


# arr = [50, 10, 40, 30, 20]

# arr.sort()  
# print(arr)





'''Sorting Using sorted() (Returns a New List)'''


# arr = [50, 10, 40, 30, 20]

# new_arr = sorted(arr)  
# print(new_arr)  
# print(arr)  






'''Sorting with Custom Key (Using lambda)'''


# arr = [53, 27, 81, 42, 19]

# arr.sort(key=lambda x: x % 10) 
# print(arr) 






'''Sorting Strings (Alphabetically)'''


# names = ["Zara", "Alice", "John", "Bob"]

# names.sort()
# print(names)






'''Sorting a List of Tuples'''


# students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]

# students.sort(key=lambda x: x[1])  
# print(students)  






'''2D Array'''


''' Creating a 2D Array (Matrix)'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# print(matrix)  






'''Accessing Elements (Indexing)'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# print(matrix[1][2])  
# print(matrix[0][0])  
# print(matrix[-1][-1])  





'''Slicing a 2D Array'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# print(matrix[1])  
# print(matrix[:2]) 





'''CRUD Operations on 2D Arrays'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# matrix.append([10, 11, 12])  
# print(matrix)





# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# for row in matrix:
#     row.append(0) 
# print(matrix)





'''Read (Accessing Data)'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# for row in matrix:
#     print(row)






'''Update (Modifying Elements)'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# matrix[1][2] = 99  
# print(matrix)





'''Delete (Removing Elements)'''


'''Remove a Specific Element'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# del matrix[1][2]  
# print(matrix)






'''Remove a Row'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# matrix.pop(1)  
# print(matrix)






'''Remove a Column from Each Row'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
# ]
# for row in matrix:
#     row.pop(1)  
# print(matrix)






'''Looping Through a 2D Array'''


'''Row-Wise Traversal'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
#  ]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()







'''Column-Wise Traversal'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
#  ]
# for col in range(len(matrix[0])):  
#     for row in matrix:
#         print(row[col], end=" ")
#     print()






'''Sorting a 2D Array'''


'''Sorting Each Row'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
#  ]
# for row in matrix:
#     row.sort()
# print(matrix)






'''Sorting by First Column'''


# matrix = [
#     [1, 2, 3],  
#     [4, 5, 6],  
#     [7, 8, 9]  
#  ]
# matrix.sort(key=lambda x: x[0])
# print(matrix)