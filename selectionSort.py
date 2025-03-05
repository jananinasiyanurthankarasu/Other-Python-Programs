#Selection sort
x = [7,3,4,2,1,8]
n = len(x)

for i in range(0,n-1):
    min_value = i
    for j in range(i+1,n):
        if x[j] < x[min_value]:
            min_value = j
    x[i],x[min_value] = x[min_value],x[i]
print(x)