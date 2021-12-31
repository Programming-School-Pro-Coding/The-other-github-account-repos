# ------------------------
# -- Strings Methods --
# ------------------------------

# split() rsplit()

a = "I love python and PHP"
print(a.split())

b = "I-love-python-and-PHP"
print(b.split("-"))

c = "I-love-python-and-PHP-and-MYSQL"
print(c.split("-", 3))

d = "I-love-python-and-PHP-and-MYSQL"
print(d.rsplit("-", 3))

# center()

e = "Mohamed"
print(e.center(9))  # spaces
print(e.center(9, "#"))  # spaces
print(e.center(15, "@"))  # spaces

# count

f = "I love python and PHP Because PHP is easy"
print(f.count("PHP"))
print(f.count("PHP", 0, 2))
print(f.count("PHP", 0, 35))


# swapcase()

g = "I love python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("P", 2, 6))
