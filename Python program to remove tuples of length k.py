#PYTHON PROGRAM TO REMOVE TUPLES OF LENGTH K

tuple_list = [(1,2), (3,4,5), (6,7), (8,9,10,11), (12,)]
k = 2
result = []
for t in tuple_list:
    if len(t) != k:
        result.append(t)
print(result)