# count the number of matching characters in the string
name1 = input("Enter the first text")
name2 = input("Enter the second text")
count = 0
for char in name1:
    if char in name2:
        count = count + 1

print(count)
