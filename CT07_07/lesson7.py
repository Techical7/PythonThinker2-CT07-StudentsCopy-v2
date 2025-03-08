import random
counter = []
Health = 100

print("Hero starts on his adventure with Health: 100")

while counter < 100:
     random_number = random.randint(1,15)
     Health -= random_number
     counter+=1

if Health < 1:
    print("After fighting monsters, his Health is now:")
    print("After fighting monsters, his Health is now:" + Health)

