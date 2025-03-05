# selection sort descending
my_array = [8,6,1,4,7,5]
n = len(my_array)
for i in range(n):
    min_value = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_value]:
            min_value = j
        my_array[j], my_array[min_value] = my_array[min_value], my_array[j]
print(my_array)
        