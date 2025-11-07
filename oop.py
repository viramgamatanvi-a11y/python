'''What is OOP?'''
''' Object-Oriented Programming'''



'''Reusability using object and class'''



'''4 Types of oop'''
'''1.Encapsulation'''
'''2.Inheritance'''
'''3.Polymorphism'''
'''4.Abstraction'''




'''Class and Object'''

'''Simple Class with Empty Attributes (Initially None)'''


# class Car:
#     brand=None
#     model=None
#     year=None
    
# car1=Car()

# print(car1.brand,car1.model,car1.year)





'''Class with Predefined (Fixed) Values'''

# class Car:
#     brand="Toyota"
#     model="Corolla"
#     year=2022
    
# car1=Car()

# print(car1.brand,car1.model,car1.year)





''' Assigning Values After Object Creation'''

# class Car:
#     brand=None
#     model=None
#     year=None

# car1=Car()

# car1.brand="Honda"
# car1.model="Civic"
# car1.year=2023

# print(car1.bra,car1.model,car1.year)






# class Car:
#     brand=None
#     model=None
#     year=None

# car1=Car()

# car1.brand="Honda"
# car1.model="Civic"
# car1.year=2023

# car2=Car()

# car2.brand="Toyota"
# car2.model="Hyryder"
# car2.year=2024

# print(car1.brand,car1.model,car1.year)
# print(car2.brand,car2.model,car2.year)





'''Constructor and Desctructor'''

'''Constructor (__init__ Method)'''


''' 1. Default Constructor (No Parameters)'''


# class Car:
#     def __init__(self):
#         print("Car object is created!")
        
# car1=Car()





'''2. Parameterized Constructor (With Parameters)'''


# class Car:
#     def __init__(self,brand,model):
#         self.barnd=brand
#         self.model=model
        
#     def show_details(self):
#         print(f"Brand : {self.barnd} , Model : {self.model}")
        
# car1=Car("Toyota","corolla")
# car1.show_details()





''' 3. Constructor with Default Arguments'''

# class Car:
#     def __init__(self,brand="Honda",model="Civic"):
#         self.brand=brand
#         self.model=model
        
#     def show_details(self):
#         print(f"Brand : {self.brand} , Mocdel : {self.model}")
        
# car1=Car()
# car1.show_details()

# car2=Car("Ford", "Mustang")
# car2.show_details()





'''Destructor (__del__ Method)'''


# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         print(f"{self.brand} Car Created!")

#     def __del__(self):
#         print(f"{self.brand} Car Destroyed!")

# car1 = Car("Tesla") 
# del car1  






'''Encapsulation'''

'''Public Methods (Getters & Setters)'''

'''With __init__ Constructor'''

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand 
#         self.model = model  

#     def set_brand(self, brand):  
#         self.brand = brand

#     def get_brand(self):  
#         return self.brand

# car1 = Car("Toyota", "Corolla")

# print(car1.get_brand())
# car1.set_brand("Honda")
# print(car1.get_brand()) 




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




'''Without __init__ Constructor'''


# class Car:
#     brand = None
#     model = None

#     def set_brand(self, brand):
#         self.brand = brand

#     def get_brand(self):
#         return self.brand

# car1 = Car()
# car1.set_brand("Ford")
# print(car1.get_brand())






''' Private Attributes (__attribute)'''

# class Car:
#     def __init__(self, brand):
#         self.__brand = brand  

#     def get_brand(self):  
#         return self.__brand  
# car1 = Car("Tesla")
# print(car1.get_brand())






'''Use Case of self vs Without self'''

# class Example:
#     def __init__(self, value):
#         self.value = value  
#     def show(self):
#         print(self.value)

# obj1 = Example(10)
# obj2 = Example(20)

# obj1.show() 
# obj2.show()






'''Without self (Class-Level Attributes)'''


# class Example:
#     value = 100  

#     def show(self):
#         print(self.value)

# obj1 = Example()
# obj2 = Example()

# obj1.show() 
# obj2.show()






'''self and del keywords'''

''' Example: Using self to Access Attributes'''

# class Car:
#     def __init__(self, brand, model):  
#         self.brand = brand  
#         self.model = model  

#     def show_details(self):  
#         print(f"Brand: {self.brand}, Model: {self.model}")


# car1 = Car("Toyota", "Corolla")
# car2 = Car("Honda", "Civic")

# car1.show_details() 
# car2.show_details() 






'''del Keyword'''

# class Car:
#     def __init__(self, brand):
#         self.brand = brand

# car1 = Car("Ford")
# print(car1.brand)  

# del car1 





'''Reflection Enbling Functions'''

'''type() → Get the Type of an Object'''

# x = 10
# print(type(x))  

# class Car:
#     pass

# car1 = Car()
# print(type(car1)) 






'''id() → Get Memory Address of an Object'''

# x = 100
# print(id(x))





'''isinstance() → Check Instance of a Class'''

# class Animal:
#     pass

# dog = Animal()
# print(isinstance(dog, Animal)) 
# print(isinstance(dog, int)) 





'''issubclass() → Check If a Class is a Subclass'''

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# print(issubclass(Dog, Animal))  
# print(issubclass(Animal, Dog))





'''dir() → List Attributes & Methods of an Object'''

# class Car:
#     def start(self):
#         pass

# car1 = Car()
# print(dir(car1))





# class Car:
#     def __init__(self):
#         self.color = "Red"

# car1 = Car()

# print(hasattr(car1, "color"))  
# print(getattr(car1, "color")) 

# setattr(car1, "color", "Blue")
# print(car1.color)  

# delattr(car1, "color")
# print(hasattr(car1, "color")) 





'''callable() → Check if an Object is Callable'''

# def greet():
#     print("Hello!")

# print(callable(greet))  
# x = 10
# print(callable(x))







'''Inheritance'''

'''Types of Inheritance with Examples'''

''' 1. Single Inheritance'''

# class Animal:  
#     def sound(self):
#         return "Makes a sound"

# class Dog(Animal):  
#     def bark(self):
#         return "Barks"

# dog = Dog()
# print(dog.sound())  
# print(dog.bark())





'''2. Multiple Inheritance'''

# class Parent1:
#     def method1(self):
#         return "Method from Parent1"

# class Parent2:
#     def method2(self):
#         return "Method from Parent2"

# class Child(Parent1, Parent2):
#     def child_method(self):
#         return "Method from Child"

# c = Child()
# print(c.method1())  
# print(c.method2())  
# print(c.child_method())





'''3. Multilevel Inheritance'''

# class Grandparent:
#     def grand_method(self):
#         return "Grandparent method"

# class Parent(Grandparent):
#     def parent_method(self):
#         return "Parent method"

# class Child(Parent):
#     def child_method(self):
#         return "Child method"

# c = Child()
# print(c.grand_method())  
# print(c.parent_method())  
# print(c.child_method())





''' 4. Hierarchical Inheritance'''

# class Parent:
#     def parent_method(self):
#         return "Parent method"

# class Child1(Parent):
#     def child1_method(self):
#         return "Child1 method"

# class Child2(Parent):
#     def child2_method(self):
#         return "Child2 method"

# c1 = Child1()
# c2 = Child2()

# print(c1.parent_method())  
# print(c2.parent_method())





'''5. Hybrid Inheritance'''

# class A:
#     def method_A(self):
#         return "Method from A"

# class B(A):
#     def method_B(self):
#         return "Method from B"

# class C(A):
#     def method_C(self):
#         return "Method from C"

# class D(B, C):
#     def method_D(self):
#         return "Method from D"

# obj = D()
# print(obj.method_A())  
# print(obj.method_B()) 
# print(obj.method_C()) 
# print(obj.method_D()) 






'''Constructor Inheritance'''

'''Using Parent Class Constructor (Implicitly)'''

# class Parent:
#     def __init__(self):
#         print("Parent Constructor Called")

# class Child(Parent):
#     pass

# obj = Child()





''' Overriding the Parent Class Constructor'''

# class Parent:
#     def __init__(self):
#         print("Parent Constructor Called")

# class Child(Parent):
#     def __init__(self):
#         print("Child Constructor Called")  

# obj = Child()





'''Calling Parent Constructor using super()'''

# class Parent:
#     def __init__(self):
#         print("Parent Constructor Called")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child Constructor Called")

# obj = Child()





''' Passing Arguments to Parent Constructor using super()'''

# class Parent:
#     def __init__(self, name):
#         print(f"Parent Constructor: {name}")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name) 
#         print(f"Child Constructor: Age {age}")

# obj = Child("John", 25)





'''Using super() with Multiple Inheritance'''

# class A:
#     def __init__(self):
#         print("Constructor of A")

# class B(A):
#     def __init__(self):
#         super().__init__()  
#         print("Constructor of B")

# class C(B):
#     def __init__(self):
#         super().__init__()  
#         print("Constructor of C")

# obj = C()






'''issubclass() and super() methods'''

'''1. issubclass() Method'''

''' Example 1: Checking Subclass Relationship'''

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# print(issubclass(Dog, Animal))  
# print(issubclass(Animal, Dog)) 
# print(issubclass(Dog, object))  





'''Example 2: Checking Multiple Parent Classes'''

# class A: pass
# class B: pass
# class C(A, B): pass  

# print(issubclass(C, (A, B)))  
# print(issubclass(A, (B, C))) 





''' 2. super() Method'''

''' Example 1: Using super() to Call Parent Constructor'''

# class Parent:
#     def __init__(self):
#         print("Parent Constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()  
#         print("Child Constructor")

# obj = Child()





'''Example 2: Using super() to Call Parent Method'''

# class Parent:
#     def show(self):
#         print("Parent Method")

# class Child(Parent):
#     def show(self):
#         super().show()  
#         print("Child Method")

# obj = Child()
# obj.show()





'''Example 3: super() in Multiple Inheritance'''

# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         super().show()  
#         print("Class B")

# class C(B):
#     def show(self):
#         super().show()  
#         print("Class C")

# obj = C()
# obj.show()






'''Polymorphism'''

'''Method Overriding (Polymorphism in Inheritance)'''

# class Animal:
#     def sound(self):
#         print("Animals make sounds")

# class Dog(Animal):
#     def sound(self):  
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):  
#         print("Cat meows")


# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()  
# d.sound()  
# c.sound()  





'''Method Overloading (Achieved Using Default Arguments)'''

# class Math:
#     def add(self, a, b=0, c=0):
#         return a + b + c  

# m = Math()
# print(m.add(5))       
# print(m.add(5, 10))  
# print(m.add(5, 10, 15))






''' Operator Overloading'''

# class Box:
#     def __init__(self, volume):
#         self.volume = volume

#     def __add__(self, other):  
#         return Box(self.volume + other.volume)

# b1 = Box(10)
# b2 = Box(20)
# b3 = b1 + b2  

# print(b3.volume) 




''' Polymorphism with Functions'''

# class Car:
#     def fuel_type(self):
#         return "Petrol"

# class ElectricCar:
#     def fuel_type(self):
#         return "Electric"

# def show_fuel(vehicle):
#     print(vehicle.fuel_type())

# c = Car()
# e = ElectricCar()

# show_fuel(c)  
# show_fuel(e)




'''Operator Overloading'''

''' Operator Overloading with + (Addition Operator)'''

# class Box:
#     def __init__(self, volume):
#         self.volume = volume

#     def __add__(self, other):  
#         return Box(self.volume + other.volume)

# b1 = Box(10)
# b2 = Box(20)
# b3 = b1 + b2  

# print(b3.volume)





'''Overloading * (Multiplication Operator)'''

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __mul__(self, other):
#         return Number(self.value * other.value)

# n1 = Number(5)
# n2 = Number(3)
# n3 = n1 * n2  

# print(n3.value)




'''Overloading > (Comparison Operator)'''

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __gt__(self, other):  
#         return self.marks > other.marks

# s1 = Student(85)
# s2 = Student(90)

# print(s1 > s2) 





''' Overloading == (Equality Operator)'''

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __eq__(self, other):  
#         return self.name == other.name

# p1 = Person("Alice")
# p2 = Person("Bob")
# p3 = Person("Alice")

# print(p1 == p2) 
# print(p1 == p3)




'''Overloading - (Subtraction Operator)'''

# class Amount:
#     def __init__(self, value):
#         self.value = value

#     def __sub__(self, other):
#         return Amount(self.value - other.value)

# a1 = Amount(50)
# a2 = Amount(20)
# a3 = a1 - a2  

# print(a3.value) 





'''Abstraction'''

'''Abstract Class and Abstract Method'''

# from abc import ABC, abstractmethod

# class Vehicle(ABC):  
#     @abstractmethod
#     def start(self): 
#         pass

# class Car(Vehicle):  
#     def start(self):
#         print("Car starts with a key")

# class Bike(Vehicle):  
#     def start(self):
#         print("Bike starts with a button")


# c = Car()
# b = Bike()

# c.start()  
# b.start()  





'''Abstract Class with Constructor'''

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name  
    
#     @abstractmethod
#     def make_sound(self):
#         pass  

# class Dog(Animal):
#     def make_sound(self):
#         return f"{self.name} says Woof!"

# d = Dog("Buddy")
# print(d.make_sound())  





'''Use Case: Banking System'''

# from abc import ABC, abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def withdraw(self, amount):
#         pass

# class SavingsAccount(Bank):
#     def withdraw(self, amount):
#         print(f"Withdrawing {amount} from Savings Account")

# class CurrentAccount(Bank):
#     def withdraw(self, amount):
#         print(f"Withdrawing {amount} from Current Account")

# s = SavingsAccount()
# c = CurrentAccount()

# s.withdraw(500) 
# c.withdraw(1000)