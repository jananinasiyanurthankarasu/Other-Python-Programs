#Program to replace duplicate occurences in the string

str = "Hello world"
str1 = " "
for i in range(len(str)):
    if i != 2:
        str1 = str1 + str[i]
print(str1)
