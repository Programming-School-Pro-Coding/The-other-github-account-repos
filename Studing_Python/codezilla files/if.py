is_hungry = False #input("Do you hungry : ")
wants_to_eat = True #input("Do you want to eat : ")

if is_hungry and wants_to_eat == True:
    print("go eat you are hungry or just want to eat")
    print(is_hungry)
    print(wants_to_eat)
elif is_hungry and not wants_to_eat:
    print("Eat so you can survive")
    print(is_hungry)
    print(wants_to_eat)
elif wants_to_eat and not is_hungry:
    print("Eat because you can run, walk and watch TV")
    print(is_hungry)
    print(wants_to_eat)
else:
    print("do not eat because you not hungry")
    print(is_hungry)
    print(wants_to_eat)

print("The condition is finished user")