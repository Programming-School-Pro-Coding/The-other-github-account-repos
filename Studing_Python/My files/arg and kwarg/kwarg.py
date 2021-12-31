#def sum_nums(*args):
#    result = 0
#    for x in args:
#        result += x
#    return result

#print(sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))

#def my_sum(a, b, *args, option=True):
#    result = 0
#    if option:
#        for x in args:
#            result += x
#        return a + b + result
#   else:
#       return result

#print(my_sum(1, 2, 3, 4, 5, option=False))

#def make_sentence(**kwargs):
#    result = ""
#    for x in kwargs.values():
#        result += x
#    return result

#print(make_sentence(a="codezilla ", b="is ", c="awesome ", d="subscribe ", e="!"))

#def human_details(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key} : {value}")


#human_details(name="Mohamed", job="school", age="12")
#print("------------------")
#human_details(name="islam", job="developer", address="6 octoper")

def print_arg(x, y, *args, option=True, **kwargs):
    print(x, y)
    print(args)
    print(option)
    print(kwargs.items())
    print(kwargs.values())
    print(kwargs)

print_arg(1, 2, "3 is args", "4 is args", channel="codezilla")