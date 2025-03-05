# Program to remove ith character from the string

str = "Hello world"
i=2
str1 = " "
for i in range(len(str)):
    if i != 2:
        str1 = str1 +str[i]
print(str1)