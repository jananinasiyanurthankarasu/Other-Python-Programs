#Python program to create a list of tuples from given list having number and its cube in each tuple
list1 = [1,2,5,6]
res = []
for val in list1:
    tup = (val,val**3)
    res.append(tup)
print(res)