#program for extracting unique values in python

testdict = {
    'gfg' : [5,6,7,8],
    'is' : [10,11,7,5],
    'best' : [6,12,10,8],
    'for' : [1,2,5]
}

mylist = []
for i in testdict.values():
    for j in i:
        if j not in mylist:
            mylist.append(j)
mylist.sort()
print(mylist)