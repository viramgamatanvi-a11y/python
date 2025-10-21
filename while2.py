
students=[]

while True:
    print("\n Welcome to our Students List!\n")
    
    print("Enter 1 for Add")
    print("Enter 2 for Update")
    print("Enter 3 for Delete")
    print("Enter 4 for View all")
    print("Enter 0 for Exit")
    
    choice=int(input("Enter your choice :"))
    
    if choice==1:
        st={
            "ID":int(input("Enter your Student ID : ")),
            "Name":input("Enter your Student Name : "),
            "City":input("Enter your Student City : ")
        }
        students.append(st)
        
        print("\n Student added successfully!\n")

    elif choice==2:
        ID=int(input("Enter your Update ID : "))
        for st in students:
            if st["ID"]==ID:
                st["Name"]=input("Enter your Update Name : ")
                st["City"]=input("Enter your Update City Name : ")
            else:
                print("Student not found")
                 
        print("\n Student Update Successfully! \n")
        
    elif choice==3:
        ID=int(input("Enter your Delete ID : "))
        
        for st in students:
            if st["ID"]==ID:
                students.remove(st)
                
        print("\n Student Delete Successfully!\n")
        
    elif choice==4:
        for st in students:
            print(f"Stusent Name : {st["Name"]}, Student City : {st["City"]}")
            
    elif choice==0:
        print("Exit")
        break
        
    else:
        print("Invalid")
        break







''' list of dicts'''


# students=[
#     {"name" : "Sumit" , "age" : 23},
#     {"name" : "Rahul" , "age" : 45},
#     {"name" : "Amit" , "age" : 67},
#     {"name" : "Vivek" , "age" : 32},
#     {"name" : "Harshil" , "age" : 43},
# ]

# print(students[3]["name"])
# print(students[3]["age"])



'''and'''



# for st in students:
#     print(st["name"],"---",st["age"])