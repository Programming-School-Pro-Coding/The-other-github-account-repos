# ------------------------
# -- Strings Methods --
# ------------------------

# replace(Old value, New value, count)

a = "Hello one Two three one one"
print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))
print(a.replace("one", "1", 3))

# join(Iterable)

mylist = ["Mohamed", "Osama", "Elsayed"]
print("-".join(mylist))
print(" ".join(mylist))
print(", ".join(mylist))
print(type("-".join(mylist)))
