#selection sort 1


arr = [22,55,1,36,77,2]
n = len(arr)

for i in range(0,n-1):
    max_element =i
    for j in range(i+1,n):
        if arr[j] < arr[max_element]:
           # max_element = j
            arr[j], arr[max_element] = arr[max_element], arr[j]
print(arr)

    