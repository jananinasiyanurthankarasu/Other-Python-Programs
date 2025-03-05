#Program to find Largest Element in the array

arr = [10,20,4]
max_element = arr[0]
n = len(arr)
for i in range(0, n):
    if arr[i] > max_element:
        max_element = arr[i]
print(max_element)