# ARMSTRONG NUMBER

x = int(input("Enter the x value"))
y = x
n = len(str(x))
sum = 0
while x > 0:
    rem = x %10
    sum = sum + pow(rem,n)
    x = x//10
if y == sum:
    print("Armstrong number")
else:
    print("Not armstrong")


