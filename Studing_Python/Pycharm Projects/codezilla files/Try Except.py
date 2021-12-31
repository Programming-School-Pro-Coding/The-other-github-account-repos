


try:
    value = int(input("Enter a number: "))
    print(value)
    print("Invalid input")
    result = 10/0
except ZeroDivisionError as err:
    print("you cannot division on zero")
except ValueError as err1:
    print(err1)


print("success")