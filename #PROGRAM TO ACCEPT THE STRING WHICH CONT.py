#PROGRAM TO ACCEPT THE STRING WHICH CONTAINS ALL VOWELS

def check(string):
    string = string.lower()
    vowels = set("aeiou")
    s = set([])
    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s) == len(vowels):
        print("string accepted")
    else:
        print("string not accepted")

string = input("Enter the string")
check(string)
