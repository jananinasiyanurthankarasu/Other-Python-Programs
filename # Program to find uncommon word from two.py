# Program to find uncommon word from two strings

string1 = "geeks for geeks and good"
word1 = string1.split()
string2 = "janani study for geeks"
word2 = string2.split()
x = []
for i in word2:
    if i not in word1:
        x.append(i)
for j in word1:
    if j not in word2:
        x.append(j)
print(x)