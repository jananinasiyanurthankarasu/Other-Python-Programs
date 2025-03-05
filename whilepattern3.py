i = 1
n = 5
while i <= n:
    print(' ' * (n -i) + '*' * (2 * i -1))
    i = i + 1
i = n-1    
while i >= 1:
    print(' ' * (n - i) + '*' * (2*i-1))
    i = i -1