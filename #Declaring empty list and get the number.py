#Declaring empty list and get the number of elements to be added in the list and the element of the list from the user

my_list = []

n = int(input("Enter the number of element to be added: "))

for i in range(1,n+1):
    element = int(input("Enter the element"))
    my_list.append(element)

print(my_list)
