# Create a file named employees.txt and write the details of 5 employees. Then read and display all the employee details.

# file = open("employees.txt", "w")
# for i in range(5):
#     name = input("Enter employee name: ")
#     age = input("Enter employee age: ")
#     salary = input("Enter employee salary: ")

#     file.write("Name: " + name + "\n")
#     file.write("Age: " + age + "\n")
#     file.write("Salary: " + salary + "\n")
#     file.write("----------------\n")

# file.close()
# file = open("employees.txt", "r")
# data = file.read()
# print("\nEmployee Details:")
# print(data)
# file.close()

2# Write a Python program to create a file named marks.txt, store 5 student marks, and append another 3 marks. Finally, read and display all the marks. 

# file = open("marks.txt", "w")
# for i in range(5):
#     mark = input("Enter student mark: ")
#     file.write(mark + "\n")
# file.close()
# file = open("marks.txt", "a")
# for i in range(3):
#     mark = input("Enter additional mark: ")
#     file.write(mark + "\n")
# file.close()
# file = open("marks.txt", "r")
# data = file.read()
# print("\nStudent Marks:")
# print(data)
# file.close()

# 3 Write a Python program to: - Create a file named shopping.txt. - Write 5 shopping items into it. - Append 2 additional items. - Read and display all items

# file = open("shopping.txt", "w")
# for i in range(5):
#     item = input("Enter shopping item: ")
#     file.write(item + "\n")
# file.close()    
# file = open("shopping.txt", "a")
# for i in range(2):
#     item = input("Enter additional shopping item: ")
#     file.write(item + "\n")
# file.close()
# file = open("shopping.txt", "r")
# data = file.read()
# print("\nShopping Items:")
# print(data)
# file.close()

# 4. Write a Python program to: - Store 10 numbers in a file. - Read the numbers from the file. - Calculate and display their sum and average

# file = open("numbers.txt", "w")
# for i in range(10):
#     number = input("Enter a number: ")
#     file.write(number + "\n")
# file.close()
# file = open("numbers.txt", "r")
# numbers = []
# for line in file:
#     numbers.append(float(line.strip()))
# file.close()
# total = sum(numbers)
# average = total / len(numbers)
# print(f"Sum: {total}")
# print(f"Average: {average}")    

# 5. Write a Python program to: - Create a file named feedback.txt. - Accept feedback from 3 users and write it into the file. - Append feedback from 2 additional users. - Read and display all feedback.

file = open("feedback.txt", "w")
for i in range(3):
    feedback = input("Enter feedback from user {}: ".format(i + 1))
    file.write(feedback + "\n")
file.close()
file = open("feedback.txt", "a")
for i in range(2):
    feedback = input("Enter additional feedback from user {}: ".format(i + 4))
    file.write(feedback + "\n")
file.close()
file = open("feedback.txt", "r")
data = file.read()
print("\nFeedback:")
print(data)
file.close()    