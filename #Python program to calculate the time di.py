#Python program to calculate the time difference in python
from datetime import datetime
val1 = datetime.now()
val2 = datetime(2019,8,3,20,20,20)
difference = val1 - val2
print(difference)
print(difference.total_seconds())
print(difference.total_seconds()/60)
print(difference.total_seconds()/60 **2)
print(difference.total_seconds()/3600)
    