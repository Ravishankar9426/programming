# file handling

# read "r" mode
# write "w"mode
# append "a"mode

# read()-->to print file contents
# write()-->to write into file
# append()-->to append string to file


# read mode-->"r"
# open("name/path", "mode")-->to open a file using python
# file1 = open("data.txt","r")
# print(file1.read()) #.read()-->read contents inside txt file
# file1.close()

# # write mode-->"w"
# # "w" to write into file by replacing text in it
# file2 = open("data.txt","w")
# print(file2.write("hi")) #.write-->to write into file
# file2.close()

# file2=open("data.txt","w")
# print(file2.write("hello today is holiday !!"))
# file2.close()

# # append mode->"a"
# file2 = open("data.txt","a")
# print(file2.write("\nhello!!!!"))
# file2.close()

# type 2

# with open("data.txt","r") as file1:
#     print(file1.read())

# with open("data.txt","w") as file2:
#     print(file2.write("how are you?"))

# with open("data.txt","a") as file3:
#     print(file3.write("\ni am fine"))

# string formatting in file handling

# file2 = open("myfile.txt","a")
# for i in range(1,101):
#     file2.write(f"\nravi {i}")
# file2.close()

# string function

# a = " ravi shankar"
# print(a.split()) #splits the string into 2






# store n names into file

n = int(input("enter the number of students:"))
file = open("myfile.txt","w")
for i in range(n):
    name = input("enter name:")
    age = input("enter age:")
    file.write(name+" "+ age +"\n")
    file.close()
    print("records saved successfully")
