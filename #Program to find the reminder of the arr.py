#Program to find the reminder of the array multiplication divided by n
arr = [1000,10]
n = 5
mul = 1
for i in range(len(arr)):
    mul = mul * arr[i]
rem = mul % n
print(rem)