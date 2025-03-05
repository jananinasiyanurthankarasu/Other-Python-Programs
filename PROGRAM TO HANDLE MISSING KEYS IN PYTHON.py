#PROGRAM TO HANDLE MISSING KEYS IN PYTHON

country_code = {
    'India' : '0091',
    'Australia' : '0025',
    'Nepal' : '00977'
}

print(country_code.get("India", "Key not Found"))
print(country_code.get("japan", "Key not Found"))