#PROGRAM TO FIND THE SIZE OF TUPLE

tuple1 = ("A", 1, "B", 2, "C", 3)
tuple2 = ("Geek1", "Raju", "Geeks2", "Nikhil", "Geek3", "Deepandhu")
tuple3 = ((1, "lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))
print("Size of Tuple1: " + str(tuple1.__sizeof__()) + " bytes")
print("Size of Tuple2: " + str(tuple2.__sizeof__()) + " bytes")
print("Size of Tuple3: " + str(tuple3.__sizeof__()) + " bytes")