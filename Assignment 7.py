# W.A.P to print below pyramid pattern "APPLE" as
# A
# AP
# APP
# APPL
# APPLE


# pattern = "APPLE"
# for i in range(1, len(pattern) + 1):
#     for j in range(i):
#         print(pattern[j], end="")
#     print()

# w.a.p to print below floyd's triangle pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# num = 1
# for i in range(1, 6):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()


def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2

    print("Your BMI is:", round(bmi, 2))

    if bmi < 15:
        print("Underweight")
    elif bmi >= 15 and bmi < 25:
        print("Normal weight")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    else:
        print("Obese")


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
calculate_bmi(weight, height)
