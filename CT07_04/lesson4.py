# print("Hello from lesson 4")

# import time
# countdown = 10

# while countdown > 0:
#     print(countdown)
#     time.sleep(1)
#     countdown -= 1
    
# else:
#     print("Happy New Year")
# Task 1a

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nuptune" ]

# Task 1b
# planets[3] = "Watch"

# for p in planets:
#     print(p)

# Task 1c

# planets.append("Pluto")
# planets.insert(3,"lalaland")

# # Task 1d
# # del(planet[5])
# planets.pop(5)

# for p in planets:
#     print(p)

# Task 2
# for p in planets:

#   if (p == "Earth"):
#     print(f"{p} this is my home")
#   elif (p == "Watch"):
#     print(f"{p} I conquered this")
#   elif (p == "lalaLand"):
#     print(f"{p} I created this")
# else:
#     print(p)

# Task 3
# countries = []

# user_inputs = ["Germany", "Japan", "end"]
# i = 0

# while True:
#     country = user_inputs[i]
#     i += 1

#     if(country.lower() == "end"):
#         break

#     countries.append(country)

# for country in countries:
#     print(f"I would like to visit [country]")

# Task 4
# list=[]

# food = ["Apple", "Banana", "Cherries", "Dates", "Eggfruit", "Fazli", "Grape", "Hackberry", "Icaco", "Jackfruit", "Kiwi", "Lime"]

# while True:
#     user_input= input("What would you like to add into the menu")

#     if(user_input.lower() == "end"):
#         break

#     food.append(user_input)

# user_input= input("What would you like to eat")
# if(user_input in food):
#     print("Please come in")
# else:
#     print("Please go next door")