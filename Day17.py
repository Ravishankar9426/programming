# import random
# print(random.randint(1, 100))
# randint() function is used to generate a random integer between the specified range. 
# In this case, it generates a random integer between 1 and 100 (inclusive). Each time you run the code, it will produce a different random number within that range.


# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(random.choice(fruits))

#COIN TOSS 

# ch = ("heads", "tails")
# print(random.choice(ch))
# z = random.randint(0,1)
# if z == 1:
#     print("Heads")
# else:
#     print("Tails")

# ch = ("rock", "paper", "scissors")
# comp = random.choice(ch)
# player = " "
# while player not in ch:
#     player = input("Enter your choice (rock, paper, scissors): ").lower()
# print(f"Player choice: {player}\nComputer choice: {comp}")

# if player == comp:
#     print("It's a tie!")

# elif comp == "rock":
#     if player == "scissors":
#         print("rock smashes scissors! Computer wins!")
#     else:
#         print("paper covers rock! player wins!")

# elif comp == "paper":
#     if player == "scissors":
#         print("scissors cut paper! player wins!")
#     elif player == "rock":
#         print("paper covers rock! computer wins!")

# elif comp == "scissors":
#     if player == "rock":
#         print("rock smashes scissors! player wins!")
#     else:
#         print("scissors cut paper! computer wins!")

# SNAKE AND LADDER GAME
# # (1,6)
# 2 player game
# initially dice = 0, if only dice is 1 game starts
# 22 ladder score -- 43
# 61 snake score -- 39

# player = "Ravi"
# enemy = "Shankar"
# playerhp = 100
# enemyhp = 100
# turn = 1
# while playerhp > 0 and enemyhp > 0:
#     print(f"Turn {turn}:")
#     player_attack = random.randint(5, 15)
#     enemy_attack = random.randint(5, 15)

#     enemyhp -= player_attack
#     playerhp -= enemy_attack

#     print(f"{player} attacks {enemy} for {player_attack} damage.")
#     print(f"{enemy} attacks {player} for {enemy_attack} damage.")
#     print(f"{player} HP: {playerhp}")
#     print(f"{enemy} HP: {enemyhp}")
#     print("-------------------------")
#     turn += 1

# import math
# print(math.sqrt(16))--> to find square root of a number
# print(math.factorial(5))--> to find factorial of a number
# print(math.pow(2, 3))--> to find power of a number
# print(math.floor(3.7))  #--> to find the largest integer less than or equal to a number
# print(math.pi)  #--> to find the value of pi

# import time
# print(time.time())--> to find the current time in seconds since the epoch (January 1, 1970) 
# print(time.ctime())  #--> to find the current local time as a struct_time object
# print(time.sleep)--> to pause the execution of the program for a specified number of seconds    

# print("hello")
# time.sleep(5)
# print("world")

# for i in range(5):
#     print("hello")
#     time.sleep(3)

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# %H --> to display the hour in 24-hour format
# %M --> to display the minute
# %S --> to display the second    
# %d--> to display the day of the month
# %m --> to display the month
# %y --> to display the year in two digits
# %p --> to display AM or PM
# %A --> to display the full weekday name
# %B--> to display the full month name

# import time as t
# print(t.strftime("%H:%M:%S"))
# print(t.strftime("%d/%m/%y %H:%M:%S"))

# OS Module-->to perform various operating system-related tasks, such as file and directory manipulation, environment variable access, and process management. It provides a way to interact with the underlying operating system in a platform-independent manner.   

import os

# os.mkdir("new_folder")--> to create a new directory named "new_folder" in the current working directory. If the directory already exists, it will raise a FileExistsError.  
# os.removedirs("new_folder")--> to remove the directory named "new_folder" and any empty parent directories. If the directory is not empty or does not exist, it will raise an error.
# os.mkdir("new_folder")
# os.rename("new_folder", "demo_folder")  #--> to rename the directory "new_folder" to "renamed_folder". If the source directory does not exist or the destination directory already exists, it will raise an error.