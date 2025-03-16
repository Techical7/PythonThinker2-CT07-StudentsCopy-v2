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