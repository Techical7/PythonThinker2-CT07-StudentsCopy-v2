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

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nuptune" ]

# # Task 1b
planets[3] = "Watch"

for p in planets:
    print(p)

# myString = ("abcde")

# for s in myString:
#     print(s)

# Task 1c

planets.append("Pluto")
planets.insert(3,"lalaland")

# Task 1d
# del(planet[5])