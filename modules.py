'''Module and it's Types'''

'''Built-in Modules'''

# import math

# print(math.sqrt(25))   
# print(math.factorial(5))  
# print(math.pi)




'''User-Defined Modules'''

'''Step 1: Create a file mymodule.py'''

# def greet(name):
#     return f"Hello, {name}!"

# pi = 3.14159




'''Step 2: Import & Use in Another File (main.py)'''

# import mymodule

# print(mymodule.greet("Alice"))  
# print(mymodule.pi)





'''Importing Specific Functions or Variables'''

# from math import sqrt, pi

# print(sqrt(16))  
# print(pi) 




'''Third-Party Modules'''

'''Example: Installing & Using requests Module'''

# import requests

# response = requests.get("https://www.google.com")
# print(response.status_code)





'''datetime module'''

'''Getting the Current Date & Time'''

# import datetime

# now = datetime.datetime.now()
# print("Current Date & Time:", now)





'''Extracting Date & Time Components'''

# now = datetime.datetime.now()

# print("Year:", now.year)
# print("Month:", now.month)
# print("Day:", now.day)
# print("Hour:", now.hour)
# print("Minute:", now.minute)
# print("Second:", now.second)






'''Creating a Custom Date & Time'''

# custom_date = datetime.datetime(2024, 10, 5, 12, 30, 45)
# print("Custom Date & Time:", custom_date)





'''Getting Only Date or Time'''

# now = datetime.datetime.now()

# print("Only Date:", now.date()) 
# print("Only Time:", now.time())





'''Formatting Dates (strftime())'''

# now = datetime.datetime.now()

# formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
# print("Formatted Date:", formatted_date)






'''Converting String to Date (strptime())'''

# date_string = "24-02-2025 14:30:45"
# converted_date = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

# print("Converted Datetime Object:", converted_date)





'''Date Arithmetic (timedelta)'''

# from datetime import datetime, timedelta

# now = datetime.now()
# new_date = now + timedelta(days=5)  
# print("New Date:", new_date)






'''time module'''

'''Getting the Current Time (time.time())'''

# import time

# import time
# current_time = time.time()
# print("Current Time (Epoch):", current_time)





'''Converting Epoch Time to Readable Format'''

# print("Readable Time:", time.ctime(current_time))




'''Getting Local Time (time.localtime())'''

# local_time = time.localtime(current_time)

# print("Year:", local_time.tm_year)
# print("Month:", local_time.tm_mon)
# print("Day:", local_time.tm_mday)
# print("Hour:", local_time.tm_hour)
# print("Minute:", local_time.tm_min)
# print("Second:", local_time.tm_sec)





'''Formatting Time (time.strftime())'''

# formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", local_time)
# print("Formatted Time:", formatted_time)





'''Converting String to Time (time.strptime())'''

# time_string = "24-02-2025 14:30:45"
# converted_time = time.strptime(time_string, "%d-%m-%Y %H:%M:%S")

# print("Converted Struct Time:", converted_time)






'''Sleeping (Delaying Execution) (time.sleep())'''

# print("Start")
# time.sleep(2)  
# print("End after 2 seconds")




'''Measuring Execution Time (time.perf_counter())'''

# start_time = time.perf_counter()


# time.sleep(1)

# end_time = time.perf_counter()

# print(f"Execution Time: {end_time - start_time} seconds")






'''math module'''

'''Basic Math Functions'''

'''Finding Square Root (math.sqrt())'''

# import math
# print(math.sqrt(25)) 


