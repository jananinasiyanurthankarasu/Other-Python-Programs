# program to check if a given string is binary or not

str = input("Enter the string")
flag =0
for char in str:
    if char!='0' and char!='1':
        flag =1
        break
if flag == 0:
    print("Binary")
else:
    print("NotBinary")