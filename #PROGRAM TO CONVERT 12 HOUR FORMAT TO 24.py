#PROGRAM TO CONVERT 12 HOUR FORMAT TO 24 HOUR FORMAT
from datetime import datetime
def f_conversion(t):
    val = datetime.strptime(t,"%I:%M:%S %p")
    return val.strftime("%H:%M:%S")

print(f_conversion("01:23:33 PM"))