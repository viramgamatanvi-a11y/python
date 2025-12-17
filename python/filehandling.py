'''What is File Handling?'''

'''Reading a File (r mode)'''

# file = open("sample.txt", "r")  
# content = file.read()
# print(content)
# file.close()




'''Writing to a File (w mode)'''

# file=open("sample.txt","w")
# file.write("Hello, Python!")
# file.close()





'''Appending to a File (a mode'''

# file=open("sample.txt","a")
# file.write("\nWelcome to python!")
# file.close()





'''Reading Line-by-Line'''

# file=open("sample.txt","r")

# print(file.readline())
# print(file.readlines())

# file.close()





'''Using with Statement (Best Practice)'''

# with open("sample.txt","r") as file:
#     content=file.read()
#     print(content)
    
    



'''Checking if File Exists Before Opening'''    

# import os

# if os.path.exists("sample.txt"):
#     with open("sample.txt", "r") as file:
#         print(file.read())
# else:
#     print("File does not exist!")




