# finding the second largest element in the list

list = [33,66,21,3,5,7,8,9]
new_list = set(list)
#print(new_list)
new_list.remove(max(new_list))
print(new_list)
print("The Second largest element is ", max(new_list))