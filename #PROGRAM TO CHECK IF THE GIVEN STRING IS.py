#PROGRAM TO CHECK IF THE GIVEN STRING IS BINARY OR NOT

str = input("Enter the string")
flag = 0
for char in str:
    if char != '1' and char != '0':
        flag = 1
        break
if flag == 0:
    print("Binary")
else:
    print("Not Binary")