# 11. Write a Python program to find the second-largest number in a list using a for loop.

# numbers = [23,25,37,44,59]
# largest = numbers[0]
# second_largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num < largest:
#         second_largest = num
# print("Second-largest number:", second_largest)

# 12. Write a Python program to count the number of uppercase and lowercase letters in a string

# text = "My name is Ravi Shankar"
# uppercase = 0
# lowercase = 0
# for letter in text:
#     if letter .isupper():
#         uppercase = uppercase + 1
#     elif letter .islower():
#         lowercase = lowercase + 1
# print("Uppercase letters:", uppercase)
# print("Lowercase letters:", lowercase)

# 13. Write a Python program to calculate the total and average of marks stored in a list.

# marks = [60,75,70,90,80]
# total = 0
# for mark in marks:
#     total = total + mark
# average = total / len(marks)
# print("Total marks:", total)
# print("Average marks:", average)

# 14. Write a Python program to find all factors of a given number using a for loop`.

number = 12
print("Factors of", number, "are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)