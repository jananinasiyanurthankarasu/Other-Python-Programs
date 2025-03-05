# REVERSE WORDS IN THE STRING

string = "geeks quiz practise code"
words = string.split()[::-1]
l = []
for i in words:
    l.append(i)
print(" ". join(l))
