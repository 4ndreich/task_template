my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
reversed_my_list = []
index = len(my_list) - 9
while index >= 0:
    list = my_list[index]
    reversed_my_list.append(list)
    index -= 1

print(reversed_my_list)   
