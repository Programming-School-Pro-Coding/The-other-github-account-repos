def sum_num(*args):
   result = 0
   for x in args:
       result += x
   return result

print(sum_num(1, 2, 3, 4, 5, 6, 7, 8, 9))

def my_sum(a, b, *args, option=True):
   result = 0
   if option:
       for x in args:
           result += x
       return  a + b + result
   else:
       return result

print(my_sum(1 , 2, 3, 4, 5, option=False))

def make_sentence(**kwargs):
   result = " "
   for x in kwargs.values():
       result += x
   return result

print(make_sentence(a="codezilla", b=" is", c=" awesome", d=" subscribe", e=" !"))

def human_details(**kwargs):
   for key, value in kwargs.items():
       print(f"{key} : {value}")

human_details(name="Anas", school=" Al Tahrer school", age=" 50")
print("-----------------------------------------------------------")
human_details(name="Mohamed", school=" Al Mohamed school")

def print_args(x, y, *args, option=True, **kwargs):
   print(x, y)
   print(args)
   print(option)
   print(kwargs)


print("Mohamed", "Anas", "Amany is args", "Ehab is args", "5 is also args", option=False, channel="codezilla", action="subscribe")

my_list = [1, 2, 3]
print(my_list)
print("-----------------------------------------------")
my_list = [1, 2, 3]
print(*my_list)

def my_sum(x, y, z):
   print(x+ y+ z)


my_list = [1, 2, 3]
my_sum(*my_list)

def my_sum(*args):
   result = 0
   for x in args:
       result += x
   return result

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print(my_sum(*list1 , *list2 , *list3))

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
a , *b, c , d = my_list
print(a)
print(b)
print(c)
print(d)

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list] # [1, 2, 3, 4, 5, 6]
print(my_merged_list)

my_first_dict = {"A":1, "B":2}
my_second_dict = {"C":3, "D":4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

list_of_char = [*"codezilla", *"Mohamed"]

print(list_of_char)

def my_sum(a, b, *args, option=True ):
   result = 0
   if option:
       for x in args:
           result += x
       return a + b + result
   else:
       return result


print(my_sum(1, 2, 3, 4, 5, option=False))

def make_sentence(**kwargs):
   result = ""
   for x in kwargs.values():
       result += x
       print(result)
   return result

print(make_sentence(a="codezilla ", b="is ", c="awesome ", d="subscribe", e=" !"))


def human_details(**kwargs):
   for key, value in kwargs.items():
       print(f"{key} : {value}")


human_details(name="Mohamed", school="Al Tahrer", age="12")
print("---------------------------")
human_details(name="islam", school="Al Tahrer", address="heliopolis")
print("---------------------------")
human_details(name="Anas", age="9")

def print_args(x, y, *args, option=True, **kwargs):
   print(x, y)
   print(args)
   print(option)
   print(kwargs)
 

print_args("Mohamed", "Anas", "Albaraa is args", "Amany is args", "5 is also args", option=False, name="Ehab is kwargs", channel="codezilla")
