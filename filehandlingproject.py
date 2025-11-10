record=[]

print("\n Welcome to our file handling project!\n")

while True:
    print("1.Create file")
    print("2.Write file")
    print("3.Append file")
    print("4.Read file")
    print("0.Exit")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        print()
        create=input("Enter your Create file name : ")    
        file=open(create,"w")
        file.write("")
        file.close()
        
        record.append(create)
        print()
        print("Your new file is created successfully!\n")
        
    elif choice==2:
        print()
        content=input("Enter your content to Write in the file :  ")
        file=open(create,"w")
        file.write(content)
        file.close()
        
        record.append(content)
        print()
        print("Your content to write in the file is successfully!\n")
        
    elif choice==3:
        print()
        append=input("Enter your Update content to Write in the file : ")
        file=open(create,"a")
        file.write(append)
        file.close()
        
        record.append(append)
        print()
        print("your Update content to Write in the file is successfullu!")
        
    elif choice==4:
        print()
        print("Your content : \n")
        
        for  i in record:
            print(i)
            
        print()
        
    elif choice==0:
        print("You are Exit for project!")
        break
    
    else:
        print("Your choice is not valid for this project!")
        break