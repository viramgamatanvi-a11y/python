'''What is OOP?'''
''' Object-Oriented Programming'''




'''Reusability using object and class'''




'''4 Types of oop'''
'''1.Encapsulation'''
'''2.Inheritance'''
'''3.Polymorphism'''
'''4.Abstraction'''





'''Class and Object'''


# class Person:
#     def greet(self):
#         print("Hello")
        
# obj=Person()
# obj2=Person()


# obj.greet()
# obj2.greet()




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
#     model="Hyryder"
#     year=2022
    
# car1=Car()

# print(car1.brand,car1.model,car1.year)





''' Assigning Values After Object Creation'''


# class Car:
#     brand=None
#     model=None
#     year=None
    
# car1=Car()

# car1.brand="Toyota"
# car1.model="Hyryder"
# car1.year=2022


# car2=Car()

# car2.brand="Tata"
# car2.model="curvv"
# car2.year=2021


# print(car1.brand,car1.model,car1.year)
# print(car2.brand,car2.model,car2.year)











































































class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def set_brand(self,brand,model):
        self.brand=brand
        self.model=model
        
    def get_brand(self):
        return self.brand,self.model
    
car1=Car("Toyota","Hyryder")

print(car1.get_brand())

car1.set_brand("Honda","i20")

print(car1.get_brand())