# print("Hello from lesson 9")
# # Recap 1
# isCorrect = False

# userInput = input("What has to be broken before you can use it? ")
# if userInput == "egg":
#     isCorrect = True
# else:
#     isCorrect = False


# if isCorrect == True:
#     print("Correct! Well done")
# else:
#     print("That's not correct. Try again! ")

userInput = input("What has to be broken before you can use it? ")

isCorrect = False

lowercase_sentence = userInput.lower()
print(lowercase_sentence)
splitted_sentence = lowercase_sentence.split()
print(splitted_sentence)
for word in splitted_sentence:
    if word == "egg":
        isCorrect = True

if isCorrect:
    print("Correct! Well Done.")
else:
    print("Thats is not correct")