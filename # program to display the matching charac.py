# program to display the matching characters in the string:
text1 = input("Enter the first text")
text2 = input("Enter the second text")

for char in set(text1):
    if char in set(text2):
        print(char)
