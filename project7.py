while True:
    print("\n===============================")
    print("Welcome to Multi-Utility toolkit")
    print("===============================\n")
    
    print("Choose an option : ")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Indentifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit\n")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        while True:
            print("Datetime and Time Operations:")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("0. Back to Main Menu\n")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                import datetime               
                now = datetime.datetime.now()
                print("Current Date and Time:", now)
                
                print("===============================\n")
                               
            elif choice==2:
                import datetime
                first=input("Enter first date (YYYY-MM-DD) : ")
                second=input("Enter second date (YYYY-MM-DD) : ")
                
                date1=datetime.datetime.strptime(first,"%Y-%m-%d")
                date2=datetime.datetime.strptime(second,"%Y-%m-%d")
                
                diffent=date2-date1
                
                print("Difference : ",diffent)
                
                print("===============================\n")
                
            elif choice==3:
                import datetime
                now=datetime.datetime.now()
                
                format=now.strftime("%d-%m-%Y %H:%M:%S")
                print("Formatted Date and time:",format)
                
                print("===============================\n")
                
            elif choice==4:
                import time
                
                print("Press Enter to start the stopwatch")
                print("Press Enter second time stopwatch stop")
                start = time.time()
                end = time.time()
                stop=start-end
                print("Stopwatch : ",stop)
                
                print("===============================\n")
                
            elif choice==0:
                print("Back to Main Menu!")
                break
                
            else:
                print("Your choice is not valid!")
                
                
    elif choice==2:
        while True:
            print("Mathematical Operations:")
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric calculations")
            print("4. Area os Geometric Shapes")
            print("0. Back to Main Menu\n")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                import math
                
                fac=int(input("Enter your number to convert factorial number : "))
                print("Factorial : ",(math.factorial(fac)))
                
                print("===============================\n")
                
            elif choice==2:
                p=int(input("Enter Principal Amount : "))
                r=int(input("Enter Rate of Interest (in %) : "))
                t=int(input("Enter time (in years) : "))
                
                a=p*(1+r/100)**t
                b=a-p
                print("Compound Interest : ",b)
                
                print("===============================\n")
                
                
            elif choice==3:
                import math
                angle=float(input("Enter angle in degrees : "))
                
                ma=math.radians(angle)
                
                sin=math.sin(angle)
                cos=math.cos(angle)
                tan=math.tan(angle)
                
                print("Sin : ",sin)
                print("Cos : ",cos)
                print("Tan : ",tan)
                
                print("===============================\n")
                
            elif choice==0:
                print("Back to Main Menu!")
                break
                
            else:
                print("Your choice is not valid!")
                
                
                
    elif choice==3:
        while True:
            print("Random Data Generation:")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Create Random Password")
            print("4. Generate Random OTP")
            print("0. Back to Main Menu\n")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                import random
                sta=int(input("Enter start number : "))
                en=int(input("Enter end number : "))
                
                num=random.randint(sta,en)
                print(f"Random number between {sta} and {en} : ",num)
                
                print("===============================\n")
                
                
            elif choice==2:
                import random
                fruits = ["apple", "banana", "cherry", "mango"]
                print(random.choice(fruits))
                
                print("===============================\n")
                
                
            elif choice==4:
                import random

                otp = random.randint(100000, 999999)
                print("Your OTP is:", otp)
                
                print("===============================\n")
                
            elif choice==0:
                print("Back to Main Menu!")
                break
                
            else:
                print("Your choice is not valid!")
                
                
    
    elif choice==4:
            print("Generate Unique Indentifiers (UUID):")
            import uuid
            id=uuid.uuid4()
            print("Generated UUID : ",id)
            
            print("===============================\n")
             
            
    elif choice==5:
        record=[]
        while True:
            print("File Operations (Custom Module):")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("0. Back to Main Menu\n")
                        
            choice=int(input("Enter your choice : ")) 
            
            if choice==1:
                create=input("Enter your Create file name : ")
                file=open(create,"w")
                file.write("")
                file.close()
                
                record.append(create)
                print("Your new file is created successfully!\n")
                
                print("===============================\n")
                
                
            elif choice==2:
                content=input("Enter your content to Write in the file :  ")
                file=open(create,"w")
                file.write(content)
                file.close()
                
                record.append(content)
                print("Your content to write in the file is successfully!\n")
                
                print("===============================\n")
                
                
            elif choice==3:
                print("File content:")
                file = open(create, "r")
                print(file.readline())
                file.close()
                
                print("===============================\n")
                

            elif choice==4:
                append=input("Enter your Update content to Write in the file : ")
                file=open(create,"a")
                file.write(append)
                file.close()
                
                record.append(append)
                print("your Update content to Write in the file is successfullu!")
                
                print("===============================\n")
                
            elif choice==0:
                print("Back to Main Menu!")
                break
                
            else:
                print("Your choice is not valid!")
                
                
    elif choice==6:
        print("Explore Module Attributes (dir()):")  
        name=input("Enter module name to explore: ")
        print(f"Available Attributes in {name} Module : ")
        print(dir(name))
        
        print("===============================\n")
        
    elif choice==7:
        print("Exiting!")
        break
        
    else:
        print("Your choice is not valid!")
        break