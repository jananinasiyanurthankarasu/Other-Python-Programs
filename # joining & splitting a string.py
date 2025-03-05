# joining & splitting a string

def split_string(string):
    str = string.split()
    return str

def join_string(string):
    str1 = "_".join(string)
    return str1

list_string = split_string("Geeks for Geeks")
print(list_string)

list_string1 = join_string(list_string)
print(list_string1)
