#sum of number of digits in the list

my_list = [12,23,45,34]
res = []
for element in my_list:
    sum =0
    for digit in str(element):
        sum = sum + int(digit)
    res.append(sum)
print(res)