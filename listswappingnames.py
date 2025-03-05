#python program to swapping of two elements in string list

name = ["Janani", "Raghu", "Kim","Pim", "Rim","Sim"]
temp = name[0]
name[0] = name[-1]
name[-1] = temp
print(name)
