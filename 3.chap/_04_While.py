from random import randint

print("Welcome to Python Casino")

pc_chocie = randint(1,10)



playing = True

user_choice = int(input("Choose number: "))
while playing:
    user_choice = int(input("Choose number:"))
    if user_choice == pc_chocie:
        print("You won!")
        playing = False
    elif user_choice > pc_chocie:
        print("Lower!", pc_chocie)
    elif user_choice < pc_chocie:
        print("Higher!", pc_chocie)
    
    
"""
if user_choice == pc_chocie:
    print("You won!")

elif user_choice > pc_choice:
    print("You Higher", pc_choice)

elif user_choice < pc_choice:
    print("You Lower", pc_choice)
"""


# While

# distance = 0

# while distance < 20:
#     print("run",distance,"km")
#     distance = distance + 1
    
