recods=[]

print("Welcome to the Student Data Organizer! \n")

while True:
    print("Select an option:")
    
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit \n")
    
    choice=int(input("Enter your choice : "))

    if choice==1:
        print("Enter student details: ")
        
        st={
            "ID":int(input("Student ID : ")),
            "Name":input("Name : "),
            "Age":int(input("Age : ")),
            "Grade":input("Grade : "),
            "Date":input("Date of Birth (YYYY-MM-DD) : "),
            "Subjects":input("Subjects (comma-separated) : ")     
        }
        
        recods.append(st)
        
        print("\n Student added successfully!\n")
        
    elif choice==2:
        print("---Display All Students---")
        for st in recods:
            print(f"Stusent ID: {st["ID"]} | Name: {st["Name"]} | Age: {st["Age"]} | Grade: {st["Grade"]} | Date of Birth : {st["Date"]} | Subjects: {st["Subjects"]}")
            print()
            
    elif choice==3:
        ID=int(input("Update ID : "))
        for st in recods:
            if st["ID"]==ID:
                st["Name"]=input("Update Name : ")
                st["Age"]=int(input("Update Age : "))
                st["Grade"]=input("Update Grade : ")
                st["Date"]=input("Update Date of Birth (YYYY-MM-DD) : ")
                st["Subjects"]=input("Update Subjects (comma-separated) : ")
                
        print("\n Student Update Successfully! \n")
                
                
    elif choice==4:
        ID=int(input("Delete ID : "))
        
        for st in recods:
            if st["ID"]==ID:
                recods.remove(st)
            
        print("\n Student Delete Successfully! \n")
        
    elif choice==5:
        ID=int(input("Display Subjects Offered ID : "))
        for st in recods:
            if st["ID"]==ID:
                print(f"Display subjects Offered : {st["Subjects"]}")
                
    elif choice==6:
        print("Exit")
        break
        
    else:
        print("Your choice is not valid!")
        break
        