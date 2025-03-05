#Adding and Subtraction of matrix


x = [
    [1,2],
    [3,4]
]

y = [
    [4,5],
    [6,7]
]

result = [
    [0,0],
    [0,0]
]

result1 = [
    [0,0],
    [0,0]
]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for i in range(len(x)):
    for j in range(len(x[0])):
        result1[i][j] = x[i][j] - y[i][j]



print(result)
print(result1)
 