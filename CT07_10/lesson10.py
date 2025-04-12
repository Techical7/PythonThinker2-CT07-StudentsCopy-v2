print("Hello from lesson 10")

# import turtle

# window = turtle.Screen()
# window.setup(600, 400)


# pen = turtle.Turtle()
# turtle.shape("turtle")
# turtle.fillcolor("orange")
# turtle.seth(0)
# turtle.pendown()
# while True:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.left(90)

# while True:
#     for i in range(5):
#         turtle.forward(100)
#         turtle.left(72)

    # window.mainloop()

var1 = 200 # global

def f():
    #var1 = 500 #local variable
    #global var2
    var2 = 500
    print(str(var2))
def f2():
    print(str(var1))


f()
print(str(var2))