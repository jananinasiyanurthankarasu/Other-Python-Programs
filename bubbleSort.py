#BUBBLE SORT
x = [2,3,1,4,7,6]
for i in range(len(x)-2):
    a = x[0]
    b = x[1]
    for j in range(len(x)-(i+1)):
        if a > b:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
        if j != len(x)-2:
            a = x[j+1]
            b = x[j+2]
print(x)