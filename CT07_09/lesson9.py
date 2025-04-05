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

import turtle

window = turtle.Screen()
window.setup(600,600)
window.screen.bgcolor("#43C7A8")

pen = turtle.turtle
pen.penup()
pen.shape("square")
pen.color("black")
pen.sety(250)



for i in range(-290,310,25):
    pen.setx(i)
    pen.stamp()

pen.goto(-300,-250)
pen.pencolor("Black")
pen = turtle.turtle
pen.pendown()
pen.seth(0)
pen.forward(600)
pen.color("yellow")
pen.hideturtle()

sally = turtle.Turtle()
sally.penup()
sally.seth(90)
sally.shape("turtle")
sally.color("red")
sally.goto(0,250)
sally.write("Sally", align="centre", font=('Arial',20))

Bob = turtle.Turtle()
Bob.penup()
Bob.seth(90)
Bob.shape("turtle")
Bob.color("blue")
Bob.goto(-200,-250)
Bob.write("Bob", align="centre", font=('Arial',20))

Keith = turtle.Turtle()
Keith.penup()
Keith.seth(90)
Keith.shape("turtle")
Keith.color("white")
Keith.goto(200,-250)
Keith.write("Keith", align="centre", font=('Arial',20))

guess = input("Guess the winner!")

sally.pendown()
Bob.pendown()
Keith
window.mainloop()