print("Welcome to the Data Analyzer and Transformer Program\n")

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def summary(record):
    print("\nData Summary:")
    print(f" - Total elements : {len(record)}")
    print(f" - Minimum value : {min(record)}")
    print(f" - Maximum value : {max(record)}")
    print(f" - Sum of all values : {sum(record)}")
    print(f" - Average value : {sum(record) / len(record):}")

def geet(record):
    return min(record), max(record), sum(record), sum(record) / len(record)

record=[]

while True:
    print("Main Menu : ")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()
    
    choice=int(input("Please enter your choice : "))
    print()
    
    if choice==1:
        first=input("Enter data for a 1D array (separated by spaces):")
        for i in first.split():
            record.append(int(i))
        print("\nData has been stored successfully!\n")
        
    elif choice == 2:
        if record:
            summary(record)
        else:
            print("No data to display.")

    elif choice == 3:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {num} is {factorial(num)}")
        
    elif choice == 4:
        threshold = int(input("Enter a threshold value to filter out data above this value: "))
        filtered = [i for i in record if i > threshold]
        print(f"Filtered Data (values >= {threshold}): {filtered}")

    elif choice == 5:
        order = int(input("Choose sorting order:\n1. Ascending\n2. Descending\nEnter your choice: "))
        if order == 1:
            record.sort()
        elif order == 2:
            record.sort(reverse=True)
        print(f"Sorted data: {record}")
        
    elif choice == 6:
        if record:
            min_value, max_value, total, avg = geet(record)
            print("\nDataset Statistics:")
            print(f" - Minimum value: {min_value}")
            print(f" - Maximum value: {max_value}")
            print(f" - Sum of all value: {total}")
            print(f" - Average value: {avg:.2f}")
        else:
            print("No data available.")

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")