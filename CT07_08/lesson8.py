print("Hello from lesson 8")

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

total_list = sorted(set(list1+list2+list3))
mid_point = len(total_list)//2
left = total_list[:mid_point]
right = total_list[mid_point:]

print(left)
print(right)