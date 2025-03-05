# Program for dictionary removing elements

this_dict = {
    "Anuradha" : 21,
    "Haritha" : 21,
    "Arushi" :22,
    "Mani" : 21
}
y = {}
for key,value in this_dict.items():
    if key != "Arushi":
        y[key] = value
print(y)