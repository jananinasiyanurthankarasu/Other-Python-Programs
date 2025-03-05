#program to find maximum and minimum k elemenets in the tuple
my_tuple = (12,5,8,19,33,7,26,15)
k = 3
sorted_list= list(my_tuple)
sorted_list.sort()
min_k_element = tuple(sorted_list[:k])
max_k_element = tuple(sorted_list[-k:])
print(min_k_element)
print(max_k_element)