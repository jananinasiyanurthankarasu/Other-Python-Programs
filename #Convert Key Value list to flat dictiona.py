#Convert Key Value list to flat dictionary

test_dict = {
    'month' : [1,2,3],
    'name' : ['jan','feb', 'mar']
}

x = list(test_dict.values())
a = x[0]
b = x[1]
d = dict()
for i in range(0,len(a)):
    d[a[i]] = b[i]
print(d)