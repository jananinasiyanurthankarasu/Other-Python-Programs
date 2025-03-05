#creating dictionary with multiple inputs for keys

data = {
    (1, "John", "Doe") : {"a": "geeks", "b" : "software", "c" :75000},
    (2,"Jane", "smith") : {"e" :30, "f" : "for", "g" : 90000},
    (3, "Bob", "Johnson") : {"h" : 35, "i" : "project", "j" : "geeks"},
    (4, "Alice", "Lee") : {"k": 40, "l" : "marketing", "m" : 100000}
}

print(data[(1, "John", "Doe")]["a"])
print(data[(2, "Jane", "smith")]["e"])
print(data[(3,"Bob", "Johnson")]["j"])

data[(1, "John", "Doe")]["a"] = {"b" : "marketing", "c" :75000}
print(data[(1, "John", "Doe")]["a"])