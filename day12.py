# break, pass , continue

# pass-->inside the loop,outside the Loop 
# break and continue--->exclusively used inside Loop 

# pass method

# age = 34
# if age < 18:
#     pass
# b = 10
# print(b)

# break method--> terminates the loop and comes out of Loop 

# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# continue method-->Skips the condition and continue executing the Loop 

# for i in range(1,11):
#     if i == 6:
#         continue
#     print(i)

# set-->unordered collection of data 
# {},unindexed,does not allow duplicates


# a ={1,2,3,4,5}
# print(type(a))

# unindexed
# fruits = {"apple", "orange", "banana", "watermelon", "pineapple"}
# print(fruits)

# set does not allow duplicate values

# a = {1,2,3,4,5,6}
# b = {4,5,6,3,2,1}
# print (a == b)

# a = {1,2,3,1,2,3,4,5,4,6,7,4,5,7}
# print(a)

# remove dupicates from list
# b = {1,2,3,1,2,3,}



# set operations

# Union 
# intersection
# difference 


# union-->"| or .union() " joins 2 set by removing duplicate values

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print (a|b)
# print (a.union(b))

# intersection-->"& or .intersection", prints only common values from 2 sets

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print (a&b)
# print (a.intersection(b) )

# difference--->"-" removes common values from specified sets

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print (a-b)
# print(b-a)


# Dictionary--> <class, 'dict'>
# {} --> represented
# key:value ---> values stored
# unindexed
# keys are unique
# using keys we call the values

# defined an empty dictionary using "{}"
# userdata = {}
# print(type(userdata))

# created a dictionary within key:value pairs of Data 
# userdata = {"name": "Ravi","age": 32, "mob no": 9656716706,"email id": "shankarr682@gmail.com"}
# print (userdata)

# error occur cause dictionary is unindexed and we can only derive the values using keys
# print(userdata[0])

# how to add values to empty dictionary

# user = {}
# user["name"] = "Ravi"
# user["age"] = 32
# user["email"]= "shankarr682@gmail.com"
# user["phone"]= 9656716706
# print(user)

# keys cannot be changed while we can change value of key using Key 
# user["name"] = "Ravi"
# user["phone"] = 9656716706
# print(user) 

# restrictions in dictionary-->keys should be unique and keys are immutable type


inbuilt functions in dictionary

a = {"name":"Ravi,"age":32,"location": "Aluva"}

dict.get(key)-->to get value of specified Key 
print(a.get("name"))
dict.keys()-->gives list of keys in dictionary
print(a.keys())
dict.values-->gives list of values in dictionary
print(a.values())
Gives value of specified keys
print(a["location"])
dict.items-->gives the list of keys:values pairs in tuple format
print(a.items())
dict.update({key:updated value})--> used to update Value
a.update({"age":33})
print(a)
dict.pop(key)--->removes corresponding key and its values
a.pop("name")
print(a)
dict.popitem()--->removes the key: value pair from end of dictionary
a.popitem()
print(a)