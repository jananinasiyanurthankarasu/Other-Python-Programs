#PROGRAM TO FIND THE WORDS WHICH ARE GREATER THAN GIVEN LENGTH K

string1 = "geeks for geeks is pdf tutorial"
word1 = string1.split()
k = 4
output = []
for i in word1:
    if len(i) > k:
        output.append(i)
print(output)
output2 = ",".join(output)
print(output2)