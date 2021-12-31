# # -----------------------
# # -- String Formatting --
# # -----------------------

# name = "Mohamed"
# age = 12
# rank = 10

# #print("My name is : "+name+" My age is: "+age+" My rank is: "+rank)

# print("My name is: {} and My age is ".format(name, age))
# print("My name is: {:s} and My age is {:d} and My rank is: {:f}".format(
#     name, age, rank))


# # {:s} => String
# # {:d} => Number
# # {:f} => float

# n = "Osama"
# l = "python"
# y = 10

# print("My name is {} I am {} Developer with {} Years EXP".format(n, l, y))

# # control floating point number

# mynum = 10
# print("My number is : {:d}".format(mynum))
# print("My number is : {:f}".format(mynum))
# print("My number is : {:.2f}".format(mynum))

# # Slice String

# mylongstring = "Hello paople of elzero web school I love you All"

# print("Message is {}".format(mylongstring))
# print("Message is {:.5s}".format(mylongstring))


# # Format Money

# myMoney = 500162350189

# print("My money in bank is: {:d}".format(myMoney))
# print("My money in bank is: {:_d}".format(myMoney))
# print("My money in bank is: {:,d}".format(myMoney))

# Arrange Items

a, b, c = "One", "Two", "Three"
# print("Hello {} {} {}".format(a, b, c))
# print("Hello {1} {2} {0}".format(a, b, c))
# print("Hello {2} {0} {1}".format(a, b, c))

x, y, z = 10, 20, 30

# print("Hello {} {} {}".format(x, y, z))
# print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
# print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# format in Verion 3.6+

myname = "Mohamed"
myage = 12
print("My name is : {myname} and My age is : {myage}")
print(f"My name is : {myname} and My age is : {myage}")
