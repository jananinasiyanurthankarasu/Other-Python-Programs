#sum of dicitionaries method 2

test_dict = {
    "a" : 100,
    "b" : 200,
    "c" :300
}
x = list(test_dict.values())
sum =0
for i in x:
    sum = sum + i
print(sum)