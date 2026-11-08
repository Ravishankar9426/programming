# num = 95
# if num < 10 or num > 50:
#     print("number is less than 10 or greater thn 50")
# else: 
#     print("not")

# age = 20
# if age <= 12:
#     print("eligible for child ticket")
# elif age >= 60:
#     print("senior citizen ticket")
# else:
#     print("normal ticket")

# age = 68
# if age < 12 or age >= 60:
#     print("eligible for special ticket")
# else:
#     print("eligible for norml ticket")

# num = 20
# if num ==10:
#  print("number is equal to 10")
# elif num ==20:
#  print("number is equal to 20")
# else:
#  print("nmber is not eqal to 10 or 20")

# num = 65
# if num ==10:
#  print("number is equal to 10")
# elif num ==20:
#  print("number is equal to 20")
# else:
#  print("number is not eqal to 10 or 20")

# num = 59
# if num < 10 or num > 50:
#     print("number is less than 10 or greater than 50")
# else:
#     print("number is not less than 10 or greater than 50")

# #strings
# strings are collection of or sequence or series or characters denoted by '',"",''''''.

# name = "month"
# print(name)
# print (type(name))

# data = "mohan's resume"
# print(data)

# say = '''Gandhi once said that "say no to violence"'''
# print(say)

# escape seqence--> used for string formatting

# \n ---> next line
# \t --->tab Space    
# \b ---> backspace 
# \\ ---> \ 

# print("my name is ravi\n my house is in aluva\t it is in ernakulam")

# raw string-->"r"

# at = '''Gandhi \b once said that \n \\"say no to violence\\"'''
# print(at)

# string concatination-->"+"

# fname = "Ravi"
# Lname = "Shankar"
# print(fname +" "+ Lname)

# A = " Ravi"
# B = "Age is 32"
# print(A + " " + B)

# A = " Ravi"
# B = 32
# print(A + " " + B)--->Cannot concatinate string and integer

#string format--> "f"

# name = "Ravi"
# age = 32
# married_status = False
# mark = 80.5
# result =f"my name is {name} and my age is {age}. My marriage status is {married_status} and my mark is {mark}"
# print(result)

# name = "Ravi"
# age = 32
# married_status = False
# mark = 80.5
# result ="my name is {name} and my age is {age}. My marriage status is {married_status} and my mark is {mark}"
# print(result)

# #typecasting---> convertion of different data into string

# name = "Ravi"
# place = "Aluva"
# mark = 98
# age = 32
# course_name = "data science"
# result = f"my name is {name} and coming from {place}. My age is {age} and marks is {mark} and have selected {course_name}"
# print(result)

# conditional statement in Python

# loop--> specified number of times a program gets executed
# while loop and for Loop 

# while loop-->condition specified Loop 
# loop gets executed till condition becomes False
# loop continues to execute when condition is True

# #syntax of while loop
# #while <condition>:
#  #code to be executed

# while true:
# print("mohan")

i = 1
while i < 10:
    print(i+1)

