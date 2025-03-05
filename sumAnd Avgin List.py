#program to find sum and avg in the list
"""
n = 1234
sum = 0
while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10
print(sum)

"""

n = [1,2,3,4,5]
sum = 0
for i in n:
    sum = sum + i
print(sum)
if sum > 0:
    avg = sum / len(n)
print(avg)