#PALINDROMe
x = input("Enter the x value")
w = ""
for i in x:
    w = i + w
if x == w:
    print("palindrome")
else:
    print("Not palidrome")