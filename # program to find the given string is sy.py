# program to find the given string is symmetrical or not

def symmetrical(mystring):
    length = len(mystring)
    if length % 2 == 0:
        mid = length // 2
    else:
        mid = length//2 +1
    start1 = 0
    start2 = mid
    flag = True
    while(start1<mid and start2 < length):
        if mystring[start1] == mystring[start2]:
            start1 += 1
            start2 += 1
        else:
            flag = False
            break
    if(flag):
        print("Symmetrical")
    else:
        print("Non Symmetrical")

symmetrical("ragu")