# ------------------------
# -- Strings Methods --
# ------------------------

# index(substring, start, end)

# a = "I love Python"
# print(a.index("P"))
# print(a.index("P", 0, 10))
# print(a.index("P", 0, 5))

# find(substring, start, end)

a = "I love Python"
print(a.find("P"))
print(a.find("l", 0, 10))
print(a.find("e", 0, 5))

# rjust(width, fill char) ljust(width, fill char)

c = "Mohamed"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Mohamed"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First line
second line
Third line"""

print(e.splitlines())
print(type(e.splitlines()))

# expandtabs()

g = "Hello\tWorld\tI\tLove\tpython"
print(g.expandtabs(20))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = "i love python"
six = "I Love Python"
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "osama_elzero100"
nine = "osama--elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbb"
y = "AaaaaBbbbb502635"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbb"
z = "AaaaaBbbbb502635"
print(u.isalnum())
print(z.isalnum())
