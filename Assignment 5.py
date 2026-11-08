# 4. Write a Python program to count the number of vowels in a given string using a for loop.

text = "My name is Rai Shankar"
count = 0
for letter in text:
    if letter in "aeiouAEIOU":
     count = count + 1
print("number of vowels:", count)

# 5. Write a Python program to find the largest number in a list using a for loop.

numbers = [14,23,35,73,85]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
        print("largest number:",largest)

# 6. Create a new list containing only odd numbers using a for loop

numbers = [10,13,18,23,29,35]
odd_numbers = []
for num in numbers:
     if num % 2 != 0:
       odd_numbers.append(num)
print("odd numbers are:", odd_numbers)

# 7. Calculate the sum of all elements in a list using a for loop

numbers =[10,20,30,40,50,60]
total = 0
for num in numbers:
    total = total + num
print("sum of all elements:", total)

# 8. Write a Python program to print all numbers divisible by 5 between 1 and 100.

for num in range(1,101):
    if num % 5 == 0:
        print(num)

# 9.Write a Python program to find the sum of the digits of a given number.

num = 13575
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of digits:", total)

# 10. Write a Python program to check whether a given number is prime using a for loop.

num = 11
if num <= 1:
    print("not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")