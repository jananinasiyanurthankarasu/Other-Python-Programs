#dictionary - sum program

thisdict = {
    "a": 100,
    "b": 200,
    "c" :300
}
sum = 0
for i in thisdict.values():
    sum = sum +i
print(sum)