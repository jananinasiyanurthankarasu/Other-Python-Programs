#Order tuple by list - Method2

test_list = [('Gfg',3),('best',9),('cs', 10), ('Geeks',2)]
ordered_list = ['Geeks', 'best', 'cs', 'Gfg']
sorted_list = []
for order in ordered_list:
    for t in test_list:
        if t[0] == order:
            sorted_list.append(t)
            break
print(sorted_list)
