# -----------------------------------
# -- Lists Methods --
# -----------------------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)


# copy()

b = [1, 2, 3, 4]
c = b.copy()
print(b)  # Main list
print(c)  # Copied list

b.append(5)

print(b)  # Main list
print(c)  # Copied list

# count()

d = [1, 2, 3, 4, 3, 9, 1, 2, 1]
print(d.count(1))

# index()

e = ["Mohamed", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "TEST")
f.insert(-1, "Test")

print(f)

# pop()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(2))
