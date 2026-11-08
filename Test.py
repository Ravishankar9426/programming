# 1. Write a program to store two numbers in variables and print their sum, difference, product, quotient and remainder.

# a = 5
# b = 6
# print( a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)

# 2. Input a number and print whether it is positive, negative or zero.

# num = 8
# if num > 0:
#     print("number is positive")
# elif num < 0:
#     print("number is negative")
# else:
#     print("zero")

# Input a person’s age. Print “Special ticket” if the age is below 12 or 60 and above; otherwise print “Normal ticket”. Use a logical operator.

# age = 24
# if age < 12 or age >= 60:
#     print("Special ticket")
# else:
#     print("Normal ticket")

# 4) Write a program to print the multiplication table of a number entered by the user, from 1 to 10.

# num = 5
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# 5. Write a program to find the sum of all numbers from 1 to 50 using a while loop.

# i = 1
# total = 0
# while i <= 50:
#     total = total + i
#     i = i + 1
# print("Sum:", total)

# 6. Write a program to print all even numbers from 1 to 100.

# for i in range(1,101):
#     if i % 2==0:
#         print(i)

# 7. Input a name and print the name in reverse order

# name = "Ravi"
# print("Reversed name:",name[::-1] )

# 8. Given the list [1, 2, 3, 2, 4, 1, 5], create and print a new list without duplicate values. Keep the first occurrence of each value.

# numbers = [1, 2, 3, 2, 4, 1, 5]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# Create a list of numbers from 1 to 10. Print the even numbers in one list and the odd numbers in another list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# even = []
# odd = []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 10. Input an integer and calculate the sum of its digits using a while Loop.

num = 1357
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of digits:", total)