#extracting unique values method2

testdict = {
    'gfg' : [5,6,7,8],
    'is' : [10,11,7,5],
    'best' : [6,12,10,8],
    'for' : [1,2,5]
}

res = []
x = list(testdict.values())
for i in x:
    for j in i:
        if j not in res:
            res.append(j)
res.sort()
print(res)