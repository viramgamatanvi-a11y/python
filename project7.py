while True:
    print("===============================")
    print("Welcome to Multi-Utility toolkit")
    print("===============================")
    
    print("Choose an option : ")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Indentifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        while True:
            print("Datetime and Time Operations:")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("0. Back to Main Menu")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                import datetime               
                now = datetime.datetime.now()
                print("Current Date and Time:", now)
                
                print("===============================")
                               
            elif choice==2:
                import datetime
                first=input("Enter first date : ")
                second=input("Enter second date : ")
                
                date1=datetime.datetime.strptime(first,"%Y-%m-%d %H:%M:%S")
                date2=datetime.datetime.strptime(second,"%Y-%m-%d %H:%M:%S")
                
                diffent=date2-date1
                
                print("Difference : ",diffent)
                
                print("===============================")
                
            elif choice==3:
                import datetime
                now=datetime.datetime.now()
                
                format=now.strftime("%d-%m-%Y %H:%M:%S")
                print("Formatted Date and time:",format)
                
                print("===============================")
                
            elif choice==4:
                import time
                
                print("Press Enter to start the stopwatch")
                print("Press Enter second time stopwatch stop")
                start = time.time()
                end = time.time()
                stop=start-end
                print("Stopwatch : ",stop)
                
                print("===============================")
                
    elif choice==2:
        while True:
            print("Mathematical Operations:")
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric calculations")
            print("4. Area os Geometric Shapes")
            print("0. Back to Main Menu")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                import math
                
                fac=int(input("Enter your number to convert factorial number : "))
                print("Factorial : ",(math.factorial(fac)))
                
                print("===============================")
                
            elif choice==2:
                p=int(input("Enter Principal Amount : "))
                r=int(input("Enter Rate of Interest (in %) : "))
                t=int(input("Enter time (in years) : "))
                
                a=p*(1+r/100)**t
                b=a-p
                print("Compound Interest : ",b)
                
                print("===============================")
                
                
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
                
                print("===============================")
                
                
    elif choice==3:
        while True:
            print("Random Data Generation:")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Create Random Password")
            print("4. Generate Random OTP")
            print("0. Back to Main Menu")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                
                
                
                   
                
                
                
    
    
