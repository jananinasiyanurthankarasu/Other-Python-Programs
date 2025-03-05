#Mergind Dictionaries - Method1

dict1 = {
    "a" :1,
    "b" :2,
    "c" :3
}
dict2 = {
    "d" :4,
    "e" :5, 
    "f" :6
}

merged_dict= {}

for key in dict1:
    merged_dict[key] = dict1[key]

for key in dict2:
    merged_dict[key] = dict2[key]

print(merged_dict)