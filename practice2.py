

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def set_brand(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def get_brand(self):
#         return self.brand,self.model
    
# car1=Car("Toyota","Hyryder")

# print(car1.get_brand())

# car1.set_brand("Honda","i20")

# print(car1.get_brand())






# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def set_brand(self,brand):
#         self.brand=brand
        
#     def get_brand(self):
#         return self.brand
    
# car1=Car("Toyota","Hyryder")

# print(car1.get_brand())

# car1.set_brand("Honda")

# print(car1.get_brand())





# class Car:
#     brand=None
#     model=None
    
#     def set_brand(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def get_brand(self):
#         return self.brand,self.model

# car1=Car()

# car1.set_brand("Fond","endo")

# print(car1.get_brand())




# class Car:
#     def __init__(self,brand):
#         self.__brand=brand
        
#     def get_brand(self):
#         return self.__brand
        
# car1=Car("Tesla")

# print(car1.get_brand())




# class Example:
#     def __init__(self,value):
#         self.value=value
        
#     def show(self):
#         print(self.value)
        
# object1=Example(10)
# object2=Example(20)


# object1.show()
# object2.show()





# class Example:
#     def __init__(self,value):
#         self.value=value
    
#     def show(self):
#         print(self.value)
        
# object1=Example(34)
# object2=Example(2+3)

# object1.show()
# object2.show()





# class Example:
#     value=100
    
#     def show(self):
#         print(self.value)
        
# object1=Example()

# object1.show()




# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def show_details(self):
#         print(f"Brand:{self.brand} , Model:{self.model}")
        
# car1=Car("Toyota","Hyryder")

# car1.show_details()




# class Car:
#     def __init__(self):
#         print("Car object is created")
        
# car1=Car()



# class Car:
#     def __init__(self,brand="Toyota",model="Hyryder"):
#         self.brand=brand
#         self.model=model
    
#     def show_details(self):
        # print(f"Brand : {self.brand} , Model : {self.model}")
        
# car1=Car()
# car1.show_details()



# car2=Car("Tata","Punch")
# car2.show_details()
 
 
 
 
 
# class Animal:
#     def sound(self):
#         return "Makes a sound"
    
# class Dog(Animal):
#     def bark(self):
#         return "Barks"
    
# dog=Dog()

# print(dog.bark())
# print(dog.sound())


# class Animal:
#     def sound(self):
#         return "Makes a sound"
    
# class Dog(Animal):
#     def bark(self):
#         return "Barks"
    
# dog=Dog()





# class Parent1:
#     def method1(self):
#         return "Method from parent1"
    
# class Parent2:
#     def method2(self):
#         return "Method from parent2"

# class Child(Parent1,Parent2):
#     def child_method(self):
#         return "Method from child"
    
# c=Child()
# print(c.method1())
# print(c.method2())
# print(c.child_method())





# class Parent1:
#     def method1(self):
#         return "method from parent1"
    
# class Parent2:
#     def method2(self):
#         return "method from parent2"
    
# class child(Parent1,Parent2):
#     def vhild_method(self):
#         return "method from child"
    
# c=child()

# print(c.method1())
# print(c.method2())
# print(c.vhild_method())



# class Grandparent:
#     def grand_method(self):
#         return "grandparent method"
    
# class parent(Grandparent):
#     def parent_method(self):
#         return "Parent method"
    
# class child(parent):
#     def child_method(self):
#         return "Child method"
    
# c=child()

# print(c.grand_method())
# print(c.parent_method())
# print(c.child_method())




# class Parent:
#     def parent_method(self):
#         return "parent method"
    
# class child1(Parent):
#     def child1_method(self):
#         return "child1 method"
    
# class child2(Parent):
#     def child2_method(self):
#         return "child2 method"
    
# c1=child1()
# c2=child2()

# print(c1.parent_method())
# print(c2.parent_method())






# class A:
#     def method_A(self):
#         return "method from A"
    
# class B(A):
#     def method_B(self):
#         return "method from B"
    
# class C(A):
#     def method_c(self):
#         return "mathod from c"
    
# class D(B,C):
#     def method_D(self):
#         return "method from D"
    
# obj=D()

# print(obj.method_A())
# print(obj.method_B())
# print(obj.method_c())
# print(obj.method_D())





# class Animal:
#     ty="4 lags"
#     def speak(self):
#         print("Animal voice")
        
# class dog(Animal):
#     pass

# obj=dog()
# print(obj.ty)

# obj.speak()




# class parent():
#     def __init__(self):
#         print("Hello")
        
# class child(parent):
#     def __init__(self):
#         print("Hello from child")
#         super().__init__()
        
# class child1(child):
#     def __init__(self):
#         print("Hello from child1")
#         super().__init__()
        
# obj=child()
# obj=child1()







# class car:
#     def __init__(self,seat,tyre):
#         self.seat=seat
#         self.tyre=tyre
        
# class Toyota(car):
#     def __init__(self, seat, tyre,ac):
#         self.ac=ac
#         super().__init__(seat, tyre)
        
#     def getdata(self):
#         print(f"Toyota: Seats - {self.seat}, Tyres - {self.tyre}, AC - {self.ac}")
        
        
# class Mahindra(car):
#     def __init__(self, seat, tyre,supersuspension):
#         self.supersuspension=supersuspension
#         super().__init__(seat, tyre)
        
#     def getdata(self):
#         print(f"Mahindra: Seats - {self.seat}, Tyres - {self.tyre}, Super Suspension - {self.supersuspension}")
       
        
# inova=Toyota(7,4,"available")
# XUV=Mahindra(5,4,"available")


# print(inova.getdata())
# print(XUV.getdata())


# toyotacars=[]
# mahindracars=[]


# while True:
    
#     print("\n Welcome to our oop list! ")

#     print("Enter 1 to add Toyota car")
#     print("Enter 2 to add Mahindra car")
#     print("Enter 3 to view all")
#     print("Enter 0 to exit")
    
#     choice=int(input("Enter your choice : "))
    
#     if choice==1:
#         seat=int(input("Enter the number of seats : "))
#         tyre=int(input("Enter the number of tyre : "))
#         ac=input("Enter the availbility of ac : ")
        
#         tobj=Toyota(seat,tyre,ac)
        
#         toyotacars.append(tobj)
        
#     elif choice==2:
#         seat=int(input("Enter the number of seats : "))
#         tyre=int(input("Enter the number of tyre : "))
#         ss=input("Enter the availbility of super suspension (y/n) : ")
        
#         mobj=Mahindra(seat,tyre,ss)
        
#         mahindracars.append(mobj)
        
#     elif choice==3:
#         print("Enter 1 to show toyota cars : ")
#         print("Enter 2 to show mahindre cars : ")
        
#         ch=int(input("Enter your choice : "))
        
#         if ch==1:
#             for obj in toyotacars:
#                 obj.getdata()
                
#         elif ch==2:
#             for obj in mahindracars:
#                 obj.getdata()

#         else:
#             print("Your choice is not valid!")

#     elif choice==0:
#         print("Exiting")
#         break
    
#     else:
#         print("Your choice is wrong")
#         break







# class Car:
#     def __init__(self, seat, tyre):
#         self.seat = seat
#         self.tyre = tyre

# class Toyota(Car):
#     def __init__(self, seat, tyre, ac):
#         super().__init__(seat, tyre)
#         self.ac = ac

#     def getdata(self):
#         print(f"Toyota: Seats - {self.seat}, Tyres - {self.tyre}, AC - {self.ac}")

# class Mahindra(Car):
#     def __init__(self, seat, tyre, supersuspension):
#         super().__init__(seat, tyre)
#         self.supersuspension = supersuspension

#     def getdata(self):
#         print(f"Mahindra: Seats - {self.seat}, Tyres - {self.tyre}, Super Suspension - {self.supersuspension}")

# toyotacars = []
# mahindracars = []

# while True:
#     print("\nWelcome to our OOP list!")
#     print("Enter 1 to add Toyota car")
#     print("Enter 2 to add Mahindra car")
#     print("Enter 3 to view all")
#     print("Enter 0 to exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         seat = int(input("Enter the number of seats: "))
#         tyre = int(input("Enter the number of tyres: "))
#         ac = input("Enter the availability of AC: ")
#         tobj = Toyota(seat, tyre, ac)
#         toyotacars.append(tobj)

#     elif choice == 2:
#         seat = int(input("Enter the number of seats: "))
#         tyre = int(input("Enter the number of tyres: "))
#         ss = input("Enter the availability of super suspension: ")
#         mobj = Mahindra(seat, tyre, ss)
#         mahindracars.append(mobj)

#     elif choice == 3:
#         print("Enter 1 to show Toyota cars: ")
#         print("Enter 2 to show Mahindra cars: ")
#         ch = int(input("Enter your choice: "))

#         if ch == 1:
#             for obj in toyotacars:
#                 obj.getdata()
#         elif ch == 2:
#             for obj in mahindracars:
#                 obj.getdata()
#         else:
#             print("Your choice is not valid!")

#     elif choice == 0:
#         print("Exiting")
#         break

#     else:
#         print("Your choice is wrong")
#         break












# class Car:
#     def __init__(self,seat,tyre):
#         self.seat=seat
#         self.tyre=tyre
        
# class Toyota(Car):
#     def __init__(self, seat, tyre,ac):
#         super().__init__(seat, tyre)
#         self.ac=ac
        
#     def getdata(self):
#         print(f"Toyota: Seats - {self.seat} , Tyres - {self.tyre} , AC - {self.ac}")
        
# class Mahindra(Car):
#     def __init__(self, seat, tyre, supersuspension):
#         super().__init__(seat, tyre)
#         self.supersuspension=supersuspension
    
#     def getdata(self):
#         print(f"Mahindra: Seats - {self.seat} , Tyres - {self.tyre} , supersuspension - {self.supersuspension}")
        
    
    
# toyotacars=[]
# mahindracars=[]


# while True:
#     print("Welcome to our oop list!\n")
    
#     print("Enter 1 to add toyota car")
#     print("Enter 2 to add mahindra car")
#     print("Entre 3 to view all")
#     print("Enter 0 to exit")
    
#     choice=int(input("Enter your choice : "))
    
#     if choice==1:
#         seat=int(input("Enter the number of seats : "))
#         tyre=int(input("Enter the number of tyre : "))
#         ac=input("Enter the availability of seats : ")

#         tobj=Toyota(seat,tyre,ac)

#         toyotacars.append(tobj)
        
#     elif choice==2:
#         seat=int(input("Enter the number of seats : "))
#         tyre=int(input("Enter the number of tyre : "))
#         ss=input("Enter the availability of super suspension : ")
        
#         mobj=Mahindra(seat,tyre,ss)
        
#         mahindracars.append(mobj)
        
#     elif choice==3:
#         print("Enter 1 to show Toyota cars : ")
#         print("Enter 2 to show Mahindra cars : ")
        
#         ch=int(input("Enter your choice : "))
        
#         if ch==1:
#             for obj in toyotacars:
#                 obj.getdata()
        
#         elif ch==2:
#             for obj in mahindracars:
#                 obj.getdata()
                
#         else:
#             print("Your choice is not valid!")
            
#     elif choice==0:
#         print("Exiting")
#         break
    
#     else:
#         print("Your choice is Wrong!")
        
        
        


# class Employee:
#     def __init__(self,id,name,age,salary):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.salary=salary
        
#     def set_brand(self,salary,id):
#         self.salary=salary
#         self.id=id

#     def get_brand(self):
#         print(f"Employee created with id : {self.id} , name : {self.name} , age : {self.age} , salary : {self.salary}")
        

# class Manager(Employee):
#     def __init__(self, id, name, age, salary,HR,Finance):
#         super().__init__(id, name, age, salary)
#         self.HR=HR
#         self.Finance=Finance
        
#     def get_brand(self):
#         print(f"Employee created with id : {self.id} , name : {self.name} , age : {self.age} , salary : {self.salary} , HR : {self.HR} , Finance : {self.Finance}")
        
#         print(issubclass(Manager, Employee))
        
# class Developer(Employee):
#     def __init__(self, id, name, age, salary,programming_language):
#         super().__init__(id, name, age, salary)
#         self.programming_language=programming_language
        
#     def get_brand(self):
#         print(f"Employee created with id : {self.id} , name : {self.name} , age : {self.age} , salary : {self.salary} , programming_language : {self.programming_language}")
  
#         print(issubclass(Developer, Employee))
      
# Managerlist=[]
# Developerlist=[]


# while True:
    
#     print("\n --- Python OOP project: Employee Management System ---")
    
#     print("Enter 1 for Manager")
#     print("Enter 2 for Developer")
#     print("Enter 3 for show details")
#     print("Enter 0 for exit")
    
#     choice=int(input("Enter your choice : "))
    
#     if choice==1:
#         id=int(input("Enter your id : "))
#         name=input("Enter your name : ")
#         age=int(input("Enter your age : "))
#         salary=int(input("Enter your salary : "))
#         HR=input("Enter your HR : ")
#         finance=int(input("Enter your finance : "))
        
#         manag=Manager(id,name,age,salary,HR,finance)
        
#         Managerlist.append(manag)
        
#     elif choice==2:
#         id=int(input("Enter your id : "))
#         name=input("Enter your name : ")
#         age=int(input("Enter your age : "))
#         salary=int(input("Enter your salary : "))
#         programming_language=input("Enter your programming language (ex.python , java) : ")
        
#         devlop=Developer(id,name,age,salary,programming_language)
        
#         Developerlist.append(devlop)
        
#     elif choice==3:
#         print("Enter 1 to show Manager : ")
#         print("Enter 2 to show Developer : ")
        
#         ch=int(input("Enter your choice : "))
        
#         if ch==1:
#             for obj in Managerlist:
#                 obj.get_brand()
                
#         elif ch==2:
#             for obj in Developerlist:
#                 obj.get_brand()
                
#         else:
#             print("Your choice is not valid!")
            
#     elif choice==0:
#         print("Exiting!")
#         break
    
#     else:
#         print("Your choice is wrong!")




# class Example:
#         value=100
        
#         def show(self):
#                 print(self.value)
                
# obj1=Example()

# obj1.show()




# class Car:
#         brand=None
#         model=None
#         year=None
        
# car1=Car()

# print(car1.brand,car1.model,car1.year)





# class Car:
#         brand="Toyota"
#         model="Hyryder"
#         year=2023
        
# car1=Car()
# car2=Car()

# print(car1.brand,car1.model,car1.year)
# print(car2.brand,car2.model,car2.year)





# class Car:
#         brand=None
#         model=None
#         year=None
        
# car1=Car()

# car1.brand="Toyota"
# car1.model="Hyryder"
# car1.year=2023

# car2=Car()

# car2.brand="Tata"
# car2.model="curvv"
# car2.year=2024

# car3=Car()

# car3.brand="mahindre"
# car3.model="XUV"
# car3.year=2021

# car4=Car()

# car4.brand="bmw"
# car4.model="Q3"
# car4.year=2020


# print(car1.brand,car1.model,car1.year)
# print(car2.brand,car2.model,car2.year)
# print(car3.brand,car3.model,car3.year)
# print(car4.brand,car4.model,car4.year)




# class Car:
#         def __init__(self):
#                 print("car objeact is created")
                
# car1=Car()




# class Car:
#         def __init__(self,brand,model,year):
#                 self.brand=brand
#                 self.model=model
#                 self.year=year
                
#         def show_details(self):
#                 print(f"Brand : {self.brand} , Model : {self.model} , Year : {self.year}")
                
# car1=Car("Toyota","Hyryder",2023)
# car1.show_details()
                
                
                
                
# class Car:
#         def __init__(self,brand="Toyota",model="Hyryder"):
#                 self.brand=brand
#                 self.model=model
        
#         def show_details(self):
#                 print(f"Brand : {self.brand} , Model : {self.model}")
                
# car1=Car()
# car1.show_details()

# car2=Car("Tata","curvv")
# car2.show_details()






# file=open("demo.txt","r")
# content=file.read()
# print(content)
# file.close()



# file=open("demo.txt","r")
# content=file.read()
# print(content)
# file.close()




# file=open("demo.txt","w")
# file.write("Hello World!")
# file.close()



# file=open("demo.txt","w")
# file.write("Hello Tanvi!")
# file.close()



# file=open("demo.txt","a")
# file.write("Hii viramgama")

# file.close()




# file=open("demo.txt","w")
# file.write("Hello Tanvi")
# file.close()



# file=open("demo.txt","r")
# firstline=file.readline()
# firstlines=file.readlines()
# for line in firstline:
#         print(line)
        
# file.close()









# main=[]

# print("Welcome to our planner !\n")

# while True:
#     print("1.creat file")
#     print("2.write file")
#     print("3.append file")
#     print("4.read file")
#     print("0.Exit \n ")

#     choice=int(input("Enter your choice : "))

#     if choice==1:
#         print()
#         cre=input("your file name: ")
#         file=open(cre,"w")
#         file.write("")
#         file.close()

#         main.append(cre)
#         print()
#         print("your file is created ! \n")

#     elif choice==2:
#         print()
#         con=input("your content print in this file : ")
#         file=open(cre,"w")
#         file.write(con)
#         file.close()

#         main.append(con)
#         print()
#         print("your content is successfully printed in this file ! \n")

#     elif choice==3:
#         print()
#         app=input("your updeted content printed in this file : ")
#         file=open(cre,"a")
#         file.write(app)
#         file.close()

#         main.append(app)

#         print("your content updeted successfully !\n")

#     elif choice==4:
#         print()
#         print("your content : \n")

#         for i in main:
#             print(i)
#         print()

#     elif choice==0:
#         print()
#         print("Exit to our planner !\n")
#         break

#     else:
#         print()
#         print("your choice is not valid !\n")
#         break





# fill=open("sample.txt","r")
# content=fill.read()
# print(content)
# fill.close()



# my_list=[1,2,3,4,5]
# print(my_list)




# hii=my_list[0]
# hii=my_list[-1]
# hii=my_list[-2]
# print(hii)