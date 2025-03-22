# print("Hello from lesson 8")

# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]

# total_list = sorted(set(list1+list2+list3))
# mid_list = len(total_list)//2
# left = total_list[:mid_list]
# right = total_list[mid_list:]

# print(left)
# print(right)

# # task 1


# user_input = input("Password:")
# is_8char_long = False
# has_upper = False
# has_lower = False
# has_num = False
# only_alnum = False

# if len(user_input) >= 8:
#     is_8char_long  = True

# for i in user_input:
#     if i.isupper() == True:
#         has_upper = True

# for i in user_input:
#     if i.islower() == True:
#         has_lower = True

# for i in user_input:
#     if i.isdigit() == True:
#         has_num = True

# for i in user_input:
#     if i.isalnum() == True:
#         has_alnum= True



#     if is_8char_long and has_upper and has_lower and has_num is True:
#         print("Password is valid")
# else:
#     print("Invalid")

## Task 2

# Sentence = input("Sentence: ")
# output = ""
# alternate = True

# for i in Sentence:
#     if alternate:
#         output += i.upper()
#         alternate = False
#     else:
#         output += i.lower()
#         alternate = True

# print(output)

## Task 3

# sentence = "Computers empower our modern world with their digital brains"
# list = sentence.split()
# print(list)

# sentence2 = "Computers,empower,our,modern,world,with,their,digital,brains"
# list2 = sentence2.split(",")
# print(list2)

## Task 4

# words = ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# sentence = "".join(words)
# print(sentence)

# sentence2 = ",".join(words)
# print(sentence2)

# # Task 5

# text = "Hello World"
# words = text.split() ##list
# reversed_words = []

# for words in reversed(words):
#     reversed_words.append(words[::-1])

# print(reversed_words) ##list
# reversed_text = ''.join(reversed_words) ## convert list to string
# print(reversed_words)

# # Task 6
# while True:
#     word = input()
#     if(word=="end"):
#         break
#     is_palidrome = word == word[::1]
#     print(word[::1])
#     print(is_palidrome)

# # Task 7

# Word1 = input("Give me a word: ")
# text = Word1
# words = text.split() ##list
# reversed_words = []

# for words in reversed(words):
#     reversed_words.append(words[::-1])

# print(reversed_words) ##list
# reversed_text = ''.join(reversed_words) ## convert list to string
# print(reversed_words)

# Task 8

Counter = 0
while True:
    Sentence = input("Give me a sentence: ")
    if(Sentence=="end"):
        break

    is_palidrome = Sentence == Sentence[::1]
    print(Sentence[::1])
    print(is_palidrome)
Counter = Counter +1

