class Employee:
    def __init__(self,id,name,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
        
    def set_brand(self,salary,id):
        self.salary=salary
        self.id=id
        
    def get_brand(self):
        print(f"Employee created with id : {self.id} , name : {self.name} , age : {self.age} , salary : {self.salary}")
        

class Manager(Employee):
    def __init__(self, id, name, age, salary,HR,Finance):
        super().__init__(id, name, age, salary)
        self.HR=HR
        self.Finance=Finance
        
    def get_brand(self):
        print(f"Employee created with id : {self.id} , name : {self.name} , age : {self.age} , salary : {self.salary} , HR : {self.HR} , Finance : {self.Finance}")
    
    def parent(self):
        issubclass(Manager, Employee)
                                                                               
class Developer(Employee):
    def __init__(self, id, name, age, salary,programming_language):
        super().__init__(id, name, age, salary)
        self.programming_language=programming_language
        
    def get_brand(self):
        print(f"Employee created with id : {self.id} , name : {self.name} , age : {self.age} , salary : {self.salary} , programming_language : {self.programming_language}")
       
    def parent(self): 
        issubclass(Developer, Employee)

        
Managerlist=[]
Developerlist=[]


while True:
    
    print("\n --- Python OOP project: Employee Management System --- \n")
    
    print("Enter 1 for Manager")
    print("Enter 2 for Developer")
    print("Enter 3 for show details")
    print("Enter 0 for exit\n")
    
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        id=int(input("Enter your id : "))
        name=input("Enter your name : ")
        age=int(input("Enter your age : "))
        salary=int(input("Enter your salary : "))
        HR=input("Enter your HR : ")
        finance=int(input("Enter your finance : "))
        
        manag=Manager(id,name,age,salary,HR,finance)
        
        Managerlist.append(manag)
        
    elif choice==2:
        id=int(input("Enter your id : "))
        name=input("Enter your name : ")
        age=int(input("Enter your age : "))
        salary=int(input("Enter your salary : "))
        programming_language=input("Enter your programming language (ex.python , java) : ")
        
        devlop=Developer(id,name,age,salary,programming_language)
        
        Developerlist.append(devlop)
        
    elif choice==3:
        print("Enter 1 to show Manager : ")
        print("Enter 2 to show Developer : ")
        
        ch=int(input("Enter your choice : "))
        
        if ch==1:
            for obj in Managerlist:
                obj.get_brand()
                
        elif ch==2:
            for obj in Developerlist:
                obj.get_brand()
                
        else:
            print("Your choice is not valid!")
            
    elif choice==0:
        print("Exiting!")
        break
   
    else:
        print("Your choice is wrong!")
        
        
        
        