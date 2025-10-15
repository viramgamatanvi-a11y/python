# Primitive Data types

# int (integer)
# float (floating-point number)
# str (string)
# bool (boolean - True/False)
# complex (complex number)


# Ex.1
# num=34
# text="hello"
# text2='hiii'
# choice=True
# choice2=False
# point=45.6

# print(type(num))
# print(type(text))
# print(type(text2))
# print(type(choice))
# print(type(choice2))
# print(type(point)) 


# Ex.2
# print(int(34.5))
# print(int(True))
# print(str("hii"))
# print(int(False))
# print(int(45))


# Ex.3
# print(float(34.4))
# print(float(True))
# print(str("hii"))
# print(float(False))
# print(float(45))


# Ex.4
# print(bool(34.4))
# print(bool(True))
# print(bool("hii"))
# print(bool(False))
# print(bool(45))


# Ex.5
# print(str(34.4))
# print(str(True))
# print(str("hii"))
# print(str(False))
# print(str(45))


# Ex.6
# print(bool(34.4))
# print(bool(True))
# print(bool("hii"))
# print(bool(False))
# print(bool(45))
# print(bool(0))
# print(bool(1))
# print(bool(" "))


# Ex.7
# print(int(34.4))
# print(float(34))




# List data type

# 1. Create

# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# 2. Read/Access

# my_list = [1, 2, 3, 4, 5]
# first_element = my_list[0]  
# last_element = my_list[-1]
# print(first_element)
# print(last_element)

# 3. Update

# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)  
# print(my_list)   


# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2, 99)   
# print(my_list) 


# 4. Delete

# my_list = [10, 20, 30, 40, 50]
# del my_list[2]
# print(my_list)  


# my_list = ['apple', 'banana', 'cherry', 'banana']
# my_list.remove('banana')
# print(my_list) 



# my_list = [1, 2, 3, 4, 5]
# last_element = my_list.pop() 
# print(my_list)      
# second_element = my_list.pop(1)
# print(my_list)         



# Methods of List

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  


# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print(my_list)


# my_list = [1, 2, 3]
# my_list.insert(1, 4)  
# print(my_list)


# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list) 


# my_list = [1, 2, 3]
# popped_item = my_list.pop() 
# print(my_list)     
# popped_item = my_list.pop(0)
# print(my_list)      


# my_list = [10, 20, 30, 20]
# index_of_20 = my_list.index(20) 
# print(index_of_20)


# my_list = [10, 20, 30, 20]
# count_of_20 = my_list.count(20)
# print(count_of_20)


# my_list = [30, 10, 20]
# my_list.sort()
# print(my_list)



# my_list = [10, 20, 30]
# my_list.reverse()
# print(my_list)


# my_list = [10, 20, 30]
# copied_list = my_list.copy()
# print(copied_list)


# my_list = [1, 2, 3, 4, 5]

# my_list.clear()
# print(my_list) 



# Tuple data type

# 1. Create (C)

# my_tuple = (1, 2, 3, "hello", 4.5)


# 2. Read (R) or Access

# my_tuple = (1, 2, 3, "hello", 4.5)
# first_element = my_tuple[0]  
# second_element = my_tuple[3]
# print(first_element)
# print(second_element)


# my_tuple = (1, 2, 3, "hello", 4.5)
# subset = my_tuple[1:4]
# print(subset)


# Methods of Tuple

# my_tuple = (1, 2, 3, 1, 1)
# count_of_1 = my_tuple.count(1)
# print(count_of_1) 


# my_tuple = ('apple', 'banana', 'cherry')
# index_of_banana = my_tuple.index('banana')
# print(index_of_banana)


# Set data type

# 1. Create

# my_set = {1, 2, 3, 4}
# print(my_set) 
# another_set = set([3, 4, 5, 6])
# print(another_set)


# 2. Read

# my_set = {1, 2, 3, 4}
# print(1 in my_set) 
# print(5 in my_set) 


# my_set = {1, 2, 3, 4}
# for item in my_set:
#     print(item)


# 3. Update

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)


# my_set = {1, 2, 3, 4}
# my_set.update([6, 7])
# print(my_set)


# 4. Delete

# my_set = {1, 2, 3, 4, 5}
# my_set.remove(3)
# print(my_set)


# my_set = {1, 2, 3, 4, 5}
# my_set.discard(4)
# print(my_set)


# my_set = {1, 2, 3, 4, 5}
# removed_element = my_set.pop()  
# print(my_set)


# my_set = {1, 2, 3, 4, 5}
# my_set.clear()
# print(my_set)



# Methods of Set

# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)


# my_set = {1, 2, 3}
# my_set.remove(2)
# print(my_set)


# my_set = {1, 2, 3}
# my_set.discard(2)
# print(my_set) 


# my_set = {1, 2, 3}
# element = my_set.pop()  
# print(my_set) 


# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# result = set1.union(set2)
# print(result)


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.update(set2)
# print(set1)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1.intersection(set2)
# print(result)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set1.intersection_update(set2)
# print(set1)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1.difference(set2)
# print(result)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set1.difference_update(set2)
# print(set1) 


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1.symmetric_difference(set2)
# print(result)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set1.symmetric_difference_update(set2)
# print(set1)


# set1 = {1, 2}
# set2 = {1, 2, 3}
# print(set1.issubset(set2))


# set1 = {1, 2, 3}
# set2 = {1, 2}
# print(set1.issuperset(set2))


# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.isdisjoint(set2))



# Dictionary data type


# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# print(my_dict["name"])   
# print(my_dict.get("age"))



# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(my_dict.keys())



# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(my_dict.values())



# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(my_dict.items())  



# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(my_dict.get("age")) 


# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# new_data = {"city": "Los Angeles", "country": "USA"}
# my_dict.update(new_data)
# print(my_dict)  


# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# removed_value = my_dict.pop("age")
# print(removed_value) 


# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# last_item = my_dict.popitem()
# print(last_item)



# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(my_dict.setdefault("gender", "Female"))
# print(my_dict)  



# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# my_dict.clear()
# print(my_dict)

