# Level-3
# DON'T USE THE BUILT-IN FUNCTION IN PYTHON -- > reverse
def reverse_it(word):
    return word


# output
test1 = reverse_it("25Normal")
test2 = reverse_it("Libar")
test3 = reverse_it("hinkaw sabara")


print(test1.__reversed__())  # "lamroN52" printed
print(test2)  # "rabiL" printed
print(test3)  # "arabas waknih" printed
