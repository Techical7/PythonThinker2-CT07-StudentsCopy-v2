# import random
# counter = []
# Health = 100

# print("Hero starts on his adventure with Health: 100")

# while counter < 100:
#      random_number = random.randint(1,15)
#      Health -= random_number
#      counter+=1

# if Health < 1:
#     print("After fighting monsters, his Health is now:" + Health "He fought" + counter "battles, and died.")
#     print("After fighting monsters, his Health is now:" + Health)


#2
List = []
while True:
    food = input("What would you like to order?")
    if(food == "end"):
        break
    List.append(food)

for food in List:
    print("You have ordered the following:"+ food)