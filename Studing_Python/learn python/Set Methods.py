# # --------------------------
# # -- Set Methods --
# # --------------------------

# # clear()

# a = {1,2,3}
# a.clear()
# print(a)

# # union()

# b = {"One", "Two", "Three"}
# c = {"1", "2", "3"}
# x = {"Zero", "Cool"}

# print(b | c)
# print(b.union(c, x))

# # add()

# d = {1, 2, 3, 4}
# d.add(5)
# d.add(6)
# print(d)

# # copy()

# e = {1, 2, 3, 4}
# f = e.copy()

# print(e)
# print(f)

# e.add(6)

# print(e)
# print(f)

# # remove()

# g = {1, 2, 3, 4}
# g.remove(1)
# # g.remove(7)
# print(g)

# # discard

# h = {1, 2, 3, 4}
# h.discard(1)
# h.discard(7)
# print(h)

# # pop()

# i = {"A", True, 1, 2, 3, 4, 5}
# print(i.pop())

# # update()

# j = {1, 2, 3}
# k = {1, "A", "B", 2, 3}
# l = ["Html", "Css"]
# s = "Mohamed"
# n = 50
# dicT = {"Name":"Anas"}
# f = 200.5
# j.update(k, l, i, h, g, e, d, a, b, c, s, dicT)

# print(j)

# difference()

# a = {1, 2, 3, 4}
# b = {1, 2, "Osama", "Ahmed"}

# print(a)

# print(a.difference(b)) # a - b
# print(a)

# print("=" * 40) # Separator

# # difference_update()

# c = {1, 2, 3, 4}
# d = {1, 2, "Osama", "Ahmed"}

# print(c)

# c.difference_update(b) # c - d
# print(c)

# print("=" * 40) # Separator

# # intersection()

# e = {1, 2, 3, 4, "X"}
# f = {"Osama", "X", 2}
# print(e)
# print(e.intersection(f))
# print(e)

# print("=" * 40) # Separator

# # intersection_update()

# g = {1, 2, 3, 4, "X"}
# h = {"Osama", "X", 2}
# print(g)
# g.intersection_update(f)
# print(g)

# print("=" * 40) # Separator

# # symmetric_diffrence()

# i = {1,2,3,4,5,"X"}
# j = {"Osama", "Zero", 1, 2, 4, "X"}
# print(i)
# print(i.symmetric_difference(j))
# print(i)

# # symmetric_diffrence_update()

# k = {1,2,3,4,5,"X"}
# l = {"Osmama", "Zero", 1, 2, 3}
# print(k)
# k.symmetric_difference_update(l)
# print(k)

# issuperset()

a = {1,2,3,4}
b = {1,2,3}
c = {1,2,3,4,5}

print(a.issuperset(b))
print(a.issuperset(c))

print("=" * 50)

# issubset()

d = {1,2,3,4}
e = {1,2,3}
f = {1,2,3,4,5}

print(d.issubset(b))
print(d.issubset(f))

print("=" * 50)

# isdisjoint()

g = {1,2,3,4}
h = {1,2,3}
i = {10, 11, 12}

print(g.isdisjoint(h))
print(g.isdisjoint(i))