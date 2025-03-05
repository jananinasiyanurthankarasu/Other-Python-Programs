#FLATTEN TUPLE OF LIST TO TUPLE
test_tuple = ([5,6], [6,7,8,9],[3])
res = []
for i in test_tuple:
    for j in i:
        res.append(j)
res = tuple(res)
print(res)