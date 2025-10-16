recods=[]

print("\n Welcome to the Student Data Organizer! \n")

while True:
    
    print("Select an option: ")
    
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        print("Enter student details: ")
        id=input("Student ID : ")
        a=id.split(",")
        Name=input("Name : ")
        Age=int(input("Age : "))
        Grade=input("Grade : ")
        Date=input("Date of Birth (YYYY-MM-DD) : ")
        b=Date.split("-")
        print(tuple(b))
        print("/".join(b))
        Subject=set(input("Subjects (comma-separated) : ")) 
         
        st={
            "id":tuple(a),
            "Name":Name,
            "Age":Age,
            "Grade":Grade,
            "Date":tuple(b),
            "Subjects":set(Subject )   
        }    
        
        recods.append(st)
        
        print("\n Student added successfully!\n")
        
    elif choice==2:
        print("---Display All Students---")
        for st in recods:
            print(f"Stusent id: {st["id"]} | Name: {st["Name"]} | Age: {st["Age"]} | Grade: {st["Grade"]} | Date of Birth: {st["Date"]} | Subjects: {st["Subjects"]}")
            print()
            
    elif choice==3:
        id=input("Update id : ")
        a=id.split(",")
        for st in recods:
            if st["id"]==tuple(a):
                st["Name"]=input("Update Name : ")
                st["Age"]=int(input("Update Age : "))
                st["Grade"]=input("Update Grade : ")
                st["Date"]=input("Update Date of Birth (YYYY-MM-DD) : ")
                b=Date.split("-")
                print(tuple(b))
                print("/".join(b))
                st["Subjects"]=set(input("Update Subjects (comma-separated) : "))
           
        print("\n Student Update Successfully! \n")
        
    elif choice==4:
        id=input("Delete id : ")
        a=id.split(",")
        for st in recods:
            if st["id"]==tuple(a):
                thre=recods.index(st)
                del recods[thre]
                
            
        print("\n Student Delete Successfully! \n")
        
    elif choice==5:
        id=input("Display Subjects Offered id : ")
        a=id.split(",")
        for st in recods:
            if st["id"]==tuple(a):
                print(f"Display subjects Offered : {st["Subjects"]}")
                
    elif choice==6:
        print("Exit")
        break
        
    else:
        print("Your choice is not valid!")
        break
        
