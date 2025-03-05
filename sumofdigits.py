# sum of digits
n = 656
sum = 0
while n > 0:
    rem = n %10
    sum = sum + rem
    n = int(n/10)
print(sum)
