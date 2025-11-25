import numpy as np

class DataAnalytics:
    arr=None

    def create_array(self):
        print("Select the type of array to create: ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            ele=list(map(int, input("Enter element (space separated) : ").split()))
            self.array = np.array(ele)
            DataAnalytics.arr = self.array

            print("1D Numpy Array:\n", self.array)
            print()
                                        
        elif choice==2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            total = rows * cols
            print(f"Enter {total} elements for the array separated by space:")

            elements = list(map(int, input().split()))

            self.array = np.array(elements).reshape(rows, cols)
            DataAnalytics.arr = self.array

            print("\nArray Created Successfully ✔️")
            print("Your 2D Array is:\n", self.array)
            print()
               
        elif choice==3:

            x = int(input("Enter number of layers: "))
            y = int(input("Enter number of rows: "))
            z = int(input("Enter number of columns: "))

            total = x * y * z
            print(f"Enter {total} elements for the 3D array separated by space:")

            elements = list(map(int, input().split()))

            self.array = np.array(elements).reshape(x, y, z)
            DataAnalytics.arr = self.array

            print("\nArray Created Successfully ")
            print("Your 3D Array is:\n", self.array)
            print()
                
        else:
            print("Invalid choice!")
            return
            
    def math(self):
        print("\n choose a Mathematical Operetions : ")
        print("1. Addition")  
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice=int(input("Enter your choice : "))
        
        if choice == 1:
            print("\nOriginal Array:")
            print(DataAnalytics.arr)

            total = DataAnalytics.arr.size
            print(f"\nEnter {total} elements for second array:")
            elements2 = list(map(int, input().split()))

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr + arr2
            print("\nResult of Addition:")
            print(result)
            print()

        elif choice == 2:
            print("\nOriginal Array:")
            print(DataAnalytics.arr)

            total = DataAnalytics.arr.size
            print(f"\nEnter {total} elements for second array:")
            elements2 = list(map(int, input().split()))

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr - arr2
            print("\nResult of Addition:")
            print(result)
            print()

        elif choice == 3:
            print("\nOriginal Array:")
            print(DataAnalytics.arr)

            total = DataAnalytics.arr.size
            print(f"\nEnter {total} elements for second array:")
            elements2 = list(map(int, input().split()))

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr * arr2
            print("\nResult of Addition:")
            print(result)    
            print() 

        elif choice == 4:
            print("\nOriginal Array:")
            print(DataAnalytics.arr)

            total = DataAnalytics.arr.size
            print(f"\nEnter {total} elements for second array:")
            elements2 = list(map(int, input().split()))

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr / arr2
            print("\nResult of Addition:")
            print(result) 
            print()
            
        else:
            print("Invalid choice!")
            return
            
    def combin(self):
        print("Choose an option: ")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice : "))

        if choice==1:
            print("\nOriginal Array:")
            print(DataAnalytics.arr)

            total = DataAnalytics.arr.size
            print(f"\nEnter {total} elements for second array:")
            elements2 = list(map(int, input().split()))

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)
                 
            combined = np.concatenate((DataAnalytics.arr, arr2))
            print("Concatenated Array:", combined)
            print()

        elif choice==2:
            print("\nOriginal Array:")
            print(DataAnalytics.arr)

            parts = int(input("Enter number of parts to split array: "))
                
            total = DataAnalytics.arr.size
            print(f"\nEnter {total} elements for second array:")
            elements2 = list(map(int, input().split()))          

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)         

            print("\nSecond Array:")
            print(arr2)
                               
            result = np.split(DataAnalytics.arr, parts)
            print("\nSplit Arrays:",result) 
            print()
            
        else:
            print("Invalid choice!")
            return             
              
    def search(self):
        print("Choose an option : ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        
        choice=int(input("Enter your choice: "))
        
        print("\nOriginal Array :", DataAnalytics.arr)

        if choice==1:
            val = int(input("Enter value to search: "))
            result = np.where(DataAnalytics.arr == val)
            print(f"Index of {val}:", result)
            print()
            
        elif choice == 2:
            sorted_arr = np.sort(DataAnalytics.arr)
            print("Sorted Array:", sorted_arr)
            print()
                                
        elif choice == 3:
            x = int(input("Enter value to filter greater than: "))
            filtered_arr = DataAnalytics.arr[DataAnalytics.arr > x]
            print("Filtered Array:", filtered_arr)
            print()
            
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
            print()
            
        elif choice == 2:
            print("Mean:", np.mean(DataAnalytics.arr))
            print()
            
        elif choice == 3:
            print("Median:", np.median(DataAnalytics.arr))
            print()
            
        elif choice == 4:
            print("Standard Deviation:", np.std(DataAnalytics.arr))
            print()
            
        elif choice == 5:
            print("Variance:", np.var(DataAnalytics.arr))
            print()
            
        else:
            print("Invalid choice!")
            return

obj = DataAnalytics()        
while True:
    print("Welcome to the Numpy Analyzer!")
    print("=========================================")
    print("Choose an option : ")
        
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

