print("Welcome to the Interactive Personal Data Collector!")

print()

name=input("Please enter your name : ")
age=int(input("Please enter your age : "))
height=float(input("Please enter your height in meters : "))
number=int(input("Please enter your favourite number : "))

print()

print("Thank you! Here is the information we collected : ")

print()

print("Name : " ,name, ("Type : " ,type(name),"Memory Address : " ,id(name)))
print("Age : " ,age, ("Type : " ,type(age),"Memory Address : " ,id(age)))
print("Height : " ,height, ("Type : " ,type(height),"Memory Address : " ,id(height)))
print("Favourite number : " ,number, ("Type : " ,type(number),"Memory Address : " ,id(number)))

print()

Age=2025-age
print("Your birth year is approximately : ",Age, ("based on your age of ",age))

print()

print("Thank you for using the Personal Data Collector. Goodbye!")