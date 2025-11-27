import numpy as np

class DataAnalytics:
    arr=None

    def create_array(self):
        print("Select the type of array to create: ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array\n")
        
        choice=int(input("Enter your choice : "))
        if choice==1:
            ele=list(map(int, input("Enter element (space separated) : ").split()))
            self.array = np.array(ele)
            DataAnalytics.arr = self.array                           
            print("Array created successfully:\n", self.array)
                        
        elif choice==2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            total = rows * cols
            elements = list(map(int, input(f"Enter {total} elements for the array separated by space:").split()))
            self.array = np.array(elements).reshape(rows, cols)
            DataAnalytics.arr = self.array
            print("Array Created Successfully:\n",self.array)
                
        elif choice==3:
            x = int(input("Enter number of layers: "))
            y = int(input("Enter number of rows: "))
            z = int(input("Enter number of columns: "))
            total = x * y * z
            elements = list(map(int, input(f"Enter {total} elements for the 3D array separated by space:").split()))
            self.array = np.array(elements).reshape(x, y, z)
            DataAnalytics.arr = self.array
            print("Array Created Successfully:\n",self.array)
                    
        else:
            print("Invalid choice!")
            return
                       
    def math(self):
        print("\n choose a Mathematical Operetions : ")
        print("1. Addition")  
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division\n")
        
        choice=int(input("Enter your choice : "))
        if choice == 1:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            print("\nOriginal Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("\nSecond Array:")
            print(arr2)
            result = DataAnalytics.arr + arr2
            print("\nResult of Addition\n:",result)

        elif choice == 2:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"\nEnter {total} elements for second array:").split()))
            print("\nOriginal Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("\nSecond Array:")
            print(arr2)
            result = DataAnalytics.arr - arr2
            print("\nResult of Addition:\n",result)

        elif choice == 3:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"\nEnter {total} elements for second array:").split()))
            print("\nOriginal Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("\nSecond Array:")
            print(arr2)
            result = DataAnalytics.arr * arr2
            print("\nResult of Addition:\n",result)

        elif choice == 4:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"\nEnter {total} elements for second array:").split()))
            print("\nOriginal Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("\nSecond Array:")
            print(arr2)
            result = DataAnalytics.arr / arr2
            print("\nResult of Addition:\n",result)
                
        else:
            print("Invalid choice!")
            return
            
    def combin(self):
        print("Choose an option: ")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice : "))
        if choice==1:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"\nEnter {total} elements for second array:").split()))
            print("\nOriginal Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("\nSecond Array:")
            print(arr2)
            print("combine array (vertical atack) : ")      
            combined = np.concatenate((DataAnalytics.arr, arr2))
            print("Concatenated Array:\n", combined)

        elif choice==2:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"\nEnter {total} elements for second array:").split()))
            parts = int(input("Enter number of parts to split array: ")) 
            print("\nOriginal Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)         
            print("\nSecond Array:")
            print(arr2)    
            print("split array :")        
            result = np.split(DataAnalytics.arr, parts)
            print("Split Arrays:\n",result) 
                
        else:
            print("Invalid choice!")
            return            
              
    def search(self):
        print("Choose an option : ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Original Array:")
            print(DataAnalytics.arr)
            val = int(input("Enter value to search: "))
            result = np.where(DataAnalytics.arr == val)
            print(f"Index of {val}:\n", result)
                
        elif choice == 2:
            while True:
                print("1. Ascending ordered")
                print("2. Descending ordered\n")
                    
                choice=int(input("Enter your choice : "))
                    
                if choice==1:
                    print("Original Array:")
                    print(DataAnalytics.arr)
                    print()                                  
                    sorted_arr = np.sort(DataAnalytics.arr)
                    print("Ascending Sorted Array:", sorted_arr)

                elif choice==2:
                    print("Original Array:")
                    print(DataAnalytics.arr)
                    print()                                  
                    sorted_arr = np.sort(DataAnalytics.arr)[::-1]
                    print("Descending Sorted Array:", sorted_arr)
                        
                else:
                    print("Invalid choice!")
                
        elif choice == 3:
            x = int(input("Enter value to filter greater than: "))
            filtered_arr = DataAnalytics.arr[DataAnalytics.arr > x]
            print("Filtered Array:\n", filtered_arr)
        
        else:
            print("Invalid choice!")
            return
    
    def aggre(self):
        print("Choose an aggregate/statistical operation: ")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        
        choice=int(input("Enter your choice : "))
        
        print("\nOriginal Array :", DataAnalytics.arr)
        if choice==1:
            print("Sum:", np.sum(DataAnalytics.arr))
                
        elif choice == 2:
            print("Mean:", np.mean(DataAnalytics.arr))
                
        elif choice == 3:
            print("Median:", np.median(DataAnalytics.arr))
                
        elif choice == 4:
            print("Standard Deviation:", np.std(DataAnalytics.arr))
                
        elif choice == 5:
            print("Variance:", np.var(DataAnalytics.arr))
                
        else:
            print("Invalid choice!")
            return

obj = DataAnalytics()        
while True:
    print("Welcome to the Numpy Analyzer!")
    print("=========================================")
    print("Choose an option :\n ")
        
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search,sort,or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
        
    choice=int(input("Enter your choice : "))
        
    if choice == 1:
        obj.create_array()

    elif choice == 2:
        obj.math()
    
    elif choice==3:
        obj.combin()
 
    elif choice==4:
        obj.search()

    elif choice==5:
        obj.aggre()  
        
    elif choice==6:
        print("Exit")
        break 
    
    else:
        print("Your choice is not valid!")
        break     