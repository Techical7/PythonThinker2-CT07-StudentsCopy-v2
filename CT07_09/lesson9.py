# print("Hello from lesson 9")
# Recap 1

# userInput = input("What has to be broken before you can use it? ")

# isCorrect = False

# lowercase_sentence = userInput.lower()
# print(lowercase_sentence)
# splitted_sentence = lowercase_sentence.split() #list
# print(splitted_sentence)
# for word in splitted_sentence:
#     if word == "egg":
#         isCorrect = True

# if isCorrect:
#     print("Correct! Well Done.")
# else:
#     print("That is not correct! Try again")

# import random
# import turtle


# y_limit = 250
# window = turtle.Screen()
# window.setup(600,600)
# window.bgcolor("#43C7A8")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)



# for i in range(-290,310,25):
#     pen.setx(i)
#     pen.stamp()

# pen.goto(-300,-250)
# pen.pencolor("Yellow")
# # pen =turtle.Turtle()


# pen.pendown()
# pen.seth(0)
# pen.forward(600)

# pen.hideturtle()

# Sally = turtle.Turtle()
# Sally.penup()
# Sally.seth(90)
# Sally.shape("turtle")
# Sally.color("red")
# Sally.goto(0,-250)
# Sally.write("Sally", align="center", font=('Arial',20))

# Bob = turtle.Turtle()
# Bob.penup()
# Bob.seth(90)
# Bob.shape("turtle")
# Bob.color("blue")
# Bob.goto(-200,-250)
# Bob.write("Bob", align="center", font=('Arial',20))

# Keith = turtle.Turtle()
# Keith.penup()
# Keith.seth(90)
# Keith.shape("turtle")
# Keith.color("white")
# Keith.goto(200,-250)
# Keith.write("Keith", align="center", font=('Arial',20))

# guess = input("Guess the winner!")

# Sally.pendown()
# Bob.pendown()
# Keith.pendown()

# while True:
#     Sally.seth(random.randint(75,115))
#     Bob.seth(random.randint(75,115))
#     Keith.seth(random.randint(75,115))

#     Sally.forward(random.randint(1,20))
#     Bob.forward(random.randint(1,20))
#     Keith.forward(random.randint(1,20))

#     if Sally.ycor() > y_limit:
#         winner = "Sally"
#         break
#     elif Bob.ycor() > y_limit:
#         winner = "Bob"
#         break
#     elif Keith.ycor() > y_limit:
#         winner = "Keith"
#         break

# if guess == winner:
#     print("Your guess was correct")
# else:
#     print("The winner was " + winner + "! Better luck next time")

# window.mainloop()