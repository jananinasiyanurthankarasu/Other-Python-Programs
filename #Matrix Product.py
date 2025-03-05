#Matrix Product

test_list = [[1,4,5],[7,3],[4],[46,7,3]]
print("The original list", test_list)
x = []
for i in test_list:
    x.extend(i)
prod = 1
for j in x:
    prod = prod * j
print(prod)
