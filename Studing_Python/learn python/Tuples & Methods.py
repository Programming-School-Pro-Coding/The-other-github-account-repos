# # -------------------------------------
# # -- Tuple --
# # -------------------------------------


# MyAwesomeTuple = ("Osama", "Mohamed")
# MyAwesomeTuple1 = "Osama", "Mohamed"

# print(MyAwesomeTuple)
# print(MyAwesomeTuple1)

# print(type(MyAwesomeTuple))
# print(type(MyAwesomeTuple1))

# # Tuple Indexing

# MyAwesomeTuple2 = (1, 2, 3, 4, 5)
# print(MyAwesomeTuple2[0])
# print(MyAwesomeTuple2[-1])
# print(MyAwesomeTuple2[-3])

# # Tuple Assign Values

# MyAwesomeTuple3 = (1, 2, 3, 4, 5)
# # MyAwesomeTuple3[2] = "Three"

# # Tuple Items

# MyAwesomeTuple4 = ("Osama", "Osama", 1, 2, 3, 100.5, True)
# print(MyAwesomeTuple4[1])
# print(MyAwesomeTuple4[-1])


# Tuple with One Element

mytuple1 = ("Osama",)
mytuple2 = "Osama",

print(mytuple1)
print(mytuple2)

print(type(mytuple1))
print(type(mytuple2))

print(len(mytuple1))
print(len(mytuple2))

# Tuple concatenation

a = (1,2,3,4)
b = (5,6)

c = a + b
d = a + ("A", "B") + b

print(c)
print(d)

# Tuple, list, string repeat (*)

mytuple = ("A", "B")
mylist = (1, 2)
mystring = "Mohamed"

print(mystring * 6)
print(mylist * 6)
print(mytuple * 6)

# count()

a = (1,2,3,8,2,6,5,8)
print(a.count(8))

# Index()

b = (1,3,7,8,2,6,5)
# print("The position of Index Is: " + b.index(7))
print("The position of Index Is: {}".format(b.index(7)))
print(f"The position of Index Is: {b.index(7)}")

# Tuple Destruct

a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)
print(y)
print(z)