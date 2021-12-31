# -------------------
# -- lists Methods --
# -------------------

# append()
myfriend = ["Mohamed", "Osama", "Ahmed"]
myoldfriend = ["Haytham", "samah", "Ali"]

myfriend.append("Alaa")
myfriend.append("100")
myfriend.append("150.200")
myfriend.append("True")
myfriend.append(myoldfriend)
# print(myfriend)
# print(myfriend[2])
# print(myfriend[6])
# print(myfriend[7])
# print(myfriend[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

# print(a)

# remove()

x = [1, 2, 3, 4, 5, "Mohamed", True, "Osama", "Osama"]
x.remove("Osama")
# print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
w = ["Mohamed", "Ehab", "Mansour", "Mohamed", "Moustafa"]
y.sort(reverse=True)
w.sort(reverse=True)
# print(y)
# print(w)

# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
# print(z)
