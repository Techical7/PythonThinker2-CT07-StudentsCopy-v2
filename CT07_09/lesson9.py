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
window.setup(width= 600, height= 600)
window.screen.bgcolor("#43C7A8")

pen = turtle.turtle
pen.penup()
pen.seth()
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
pen.penup()





window.mainloop()