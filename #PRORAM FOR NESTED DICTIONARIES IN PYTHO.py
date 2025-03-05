#PRORAM FOR NESTED DICTIONARIES IN PYTHON

child1 = {
    "name" : "Janani",
    "age" : 20
}
child2 = {
    "name" :"Raghu",
    "age" : 30
}
child3 = {
    "name" : "Aadhya",
    "age" : 25

}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

for x,y in myfamily.items():
    print(x,y)