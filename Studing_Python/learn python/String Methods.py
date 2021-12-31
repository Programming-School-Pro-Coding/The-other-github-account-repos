# ------------------------
# -- Strings Methods --
# ------------------------------
a = "I love python"
b = "                  I love python                    "
print(len(a))
print(len(b))

a = "                  I love python                    "

print(a.strip())
print(a.rstrip())
print(a.lstrip())

print(len(a.strip()))
print(len(a.rstrip()))
print(len(a.lstrip()))


a = "##############I love python#######################"

print(a.strip())
print(a.rstrip())
print(a.lstrip())

print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

# title()

b = "I love 2d Graphics and 3g Techonology and python"
print(b.title())

# capitalize()

b = "I love 2d Graphics and 3g Techonology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "Mohamed"

print(g.upper())
print(g.lower())
