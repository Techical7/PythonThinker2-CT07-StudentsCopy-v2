# List
import random
counter = []
Health = 100
counter = str
print("Hero starts on his adventure with Health: 100")
# Random health lost
while counter < 100:
     random_number = random.randint(1,15)
     Health -= random_number
     counter+=1
# End
if Health < 1:
    print("After fighting monsters, his Health is now:" + Health "He fought" + counter "battles, and died.")
    print("After fighting monsters, his Health is now:" + Health)



# List =[]
# # Stores the item you typed in
# while True:
#     food = input("What would you like to order?")
#     if(food == "end"):
#         break
#     List.append(food)
# # food you ordered
# for food in List:
#         print("You have ordered the following:")
#         print(List)