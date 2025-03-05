#Removing keys from dicitionary

this_dict = {
    "Anuradha" : 21,
    "Haritha" : 21,
    "Arushi" :22,
    "Mani" : 21
}

#Method1:

this_dict.pop("Arushi")
print(this_dict)

#Method2:

this_dict.popitem()
print(this_dict)