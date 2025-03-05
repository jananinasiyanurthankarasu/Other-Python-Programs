#Python program to order tuples by list
tuple_list = [(2,'banana'), (3,'cherry'), (1,'apple')]
ordered_list = [1,2,3]
sorted_tuple=[]
for order in ordered_list:
    for t in tuple_list:
        if t[0] == order:
            sorted_tuple.append(t)
print(sorted_tuple)