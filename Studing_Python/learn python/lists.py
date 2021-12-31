# -------------------
# -- lists --
# -------------------

myAwesomelist = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomelist)
print(myAwesomelist[1])
print(myAwesomelist[-1])
print(myAwesomelist[-3])
# print(type(myAwesomelist[1]))

print(myAwesomelist[1:4])  # "Two", "One", 1
print(myAwesomelist[:4])
print(myAwesomelist[1:])
print(myAwesomelist[:])

print(myAwesomelist[::1])
print(myAwesomelist[::2])
print(myAwesomelist[::3])

print(myAwesomelist)
myAwesomelist[1] = 2
myAwesomelist[-1] = False
myAwesomelist[0:3] = ["A", "B", "C"]
myAwesomelist[3:5] = ["Mohamed", "Anas"]
print(myAwesomelist)
