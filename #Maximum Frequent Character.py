#Maximum Frequent Character
my_string = input("Enter the string")
my_string = "".join(my_string.split())
my_counter = {}
for letter in my_string:
    if letter in my_counter:
        my_counter[letter] += 1
    else:
        my_counter[letter] = 1

max_key = max(my_counter, key = my_counter.get)
print(str(max_key))