print("Welcome to the Pattern Generator and Number Analyzer!")
sum=0
while True:
    print()

    print("Select an option:")

    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        number=int(input("Enter the number of rows for the pattern: "))
    
        print()
    
        print("Pattern:")
        for i in range(1,number):
            print("* "*i)
            
    elif choice==2:
        start=int(input("Enter the start of the range: "))
        end=int(input("Enter the end of the range: "))
        for num in range(start,end+1):
            if num % 2==0:
                print("Number",num, "is Even")
            else:
                print("Number",num, "is Odd")
            sum=sum+num
        print("Sum of all number from",start,"to",end,"is : ",sum)
        
    elif choice==3:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("your choice is not valid!")
        break





