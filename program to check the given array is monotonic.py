# PROGRAM TO CHECK THE GIVEN ARRAY IS MONOTONIC OR NOT

a = [1,2,3,7,8,4,5]
x = []
x.extend(a)
x.sort()
y = []
y.extend(a)
y.sort(reverse = True)
if a == x or a == y:
    print("Monotic")
else:
    print("Non Monotonic")