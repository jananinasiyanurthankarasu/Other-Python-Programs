name = "janani"
name1 = []
for char in name:
    if char not in name1:
        name1.append(char)
    else:
        print("The character occuring more than once", char)

    