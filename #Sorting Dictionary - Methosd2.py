#Sorting Dictionary - Method2

original_dict = {
    "banana" : 3,
    "apple" :4,
    "Cherry" : 2,
    "date" :5
}

sorted_keys = list(original_dict.keys())

n = len(sorted_keys)

for i in range(n):
    for j in range(0,n-i-1):
        if sorted_keys[j] > sorted_keys[j+1]:
            sorted_keys[j],sorted_keys[j+1] = sorted_keys[j+1],sorted_keys[j]

sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = original_dict[key]

print(sorted_dict)