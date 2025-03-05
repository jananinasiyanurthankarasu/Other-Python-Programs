#Python program to convert nested tuple to custom key dictionary

nested_tuple= ((1,'apple'),(2, 'banana'),(3,'cherry'))
custom_dict ={}
for item in nested_tuple:
    custom_dict[item[0]] = item[1]
print(custom_dict)