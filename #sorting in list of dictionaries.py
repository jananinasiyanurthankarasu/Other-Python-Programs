#sorting in list of dictionaries

people = [
    {"name" : "Alice", "age" :25},
    {"name" : "Bob", "age" : 30},
    {"name" : "charlie", "age" : 20},
    {"name" : "David", "age" : 35}
]

sort_key = "age"

n = len(people)
for i in range(n):
    for j in range(n-i-1):
        if people[j][sort_key] > people[j+1][sort_key]:
            people[j],people[j+1] = people[j+1],people[j]

for person in people:
    print(person)
