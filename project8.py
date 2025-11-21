while True:
    print("Welcome to the Numpy Analyzer!")
    print("========================================")
    print("Choose an option : ")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Array")
    print("4. Search, Sort, or Filter Array")
    print("5. Computer Aggregates and Statistics")
    print("6. Exit")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        while True:
            print("Select the type of array to create : ")
            print("1. 1D Array")
            print("2. 2D array")
            print("3. 3D Array")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                import numpy as np
                arr = list(map(int, input("Enter your 1D array elements: ").split()))
                print(arr)