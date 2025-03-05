#Python program to sort a list of tuples by second item

list1 = [('for',24),('Geeks',8), ('Geeks', 30)]
n = len(list1)
for i in range(n):
    for j in range(n-1):
        if list1[j][1] >list1[j+1][1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)