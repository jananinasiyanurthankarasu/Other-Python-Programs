#left array rotation in python

array = [1,2,3,4,5,6]
n = len(array)
d = 2
left_rotation = array[d:] + array[:d]
print(left_rotation)